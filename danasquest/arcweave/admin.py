from django.contrib import admin
from django.core.files.base import ContentFile

from .models import ArcweaveProject, AssetFile
from django.conf import settings
import os
import json
import zipfile
import shutil


class ArcweaveProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'zip_file',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        self.unzip_and_process(obj)

    def unzip_and_process(self, obj):
        dir_path = os.path.join(settings.BASE_DIR, 'tmp')
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        with zipfile.ZipFile(obj.zip_file.path, 'r') as zip_ref:
            zip_ref.extractall(dir_path)
            self.process_files(dir_path, obj)
            shutil.rmtree(dir_path)

    def process_files(self, dir_path, obj):
        # Process JSON files first
        self.extract_json(dir_path, obj)
        # Then process other files
        for root, dirs, files in os.walk(dir_path):
            for file_name in files:
                if not file_name.endswith('.json'):
                    self.save_asset_file(obj, os.path.join(root, file_name))

    def extract_json(self, dir_path, obj):
        for root, dirs, files in os.walk(dir_path):
            for file_name in files:
                if file_name.endswith('.json'):
                    with open(os.path.join(root, file_name), 'r') as json_file:
                        data = json.load(json_file)
                        obj.json = data
                        obj.save()

    def save_asset_file(self, obj, file_path):
        with open(file_path, 'rb') as file:
            basename = os.path.basename(file_path)
            content = ContentFile(file.read())
            asset_file = AssetFile(
                project=obj,
                name=basename,
            )
            asset_file.file.save(basename, content, save=True)


class AssetFileAdmin(admin.ModelAdmin):
    list_display = ('project', 'name', 'file', 'uploaded_at', 'category')


admin.site.register(ArcweaveProject, ArcweaveProjectAdmin)
admin.site.register(AssetFile, AssetFileAdmin)
