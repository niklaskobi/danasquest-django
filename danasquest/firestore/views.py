import json
import logging

from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import UploadFileForm
from .io_functions import send_to_firestore, read_from_firestore, upload_to_cloud_storage, upload_blob_from_memory


def firestore_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save()
            # data = get_settings_file(request)
            assets = get_assets(request)
            # send_to_firestore(data, assets)

            payload = {
                "message": "Export to firestore was successful",
                "button_link":
                    {
                        "link": reverse('home'),
                        "label": "ok, nice, now go back"
                    }
            }
            return render(request, 'arcweave/export_succesfull.html', payload)
    else:
        form = UploadFileForm()
    return render(request, 'arcweave/export_to_firestore.html', {'form': form})


def view_uploaded_chunks(request):
    data = read_from_firestore()
    # print(f'Data from firestore document: {data}')
    upload_to_cloud_storage()

    return render(request, 'arcweave/view_uploaded.html', {'data': data})




def get_settings_file(request):
    file = request.FILES['project_settings']
    logging.debug(f"Handling uploaded file: {file.name}")
    data = file.read().rstrip()
    data_json = clean_string_for_json(data.decode())
    logging.debug(f"Json data from uploaded file: {data_json}")
    return data_json


def get_assets(request):
    assets_list = []
    if 'pic_cover' in request.FILES:
        assets_list.append({'name': 'pic_cover', 'file': request.FILES['pic_cover'].file})
        # upload_blob_from_memory(request.FILES['pic_cover'].file, 'pic_cover')
        # upload_blob_from_memory('test', 'pic_cover')

    # if 'pic_characters' in request.FILES:
    #     assets_list.append(request.FILES['pic_characters'])
    # if 'pic_backgrounds' in request.FILES:
    #     assets_list.append(request.FILES['pic_backgrounds'])
    return assets_list


def clean_string_for_json(value):
    removed_newlines = ''.join(value.splitlines())
    json_str = json.loads(removed_newlines)
    return json_str
