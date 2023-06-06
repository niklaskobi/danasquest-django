from django.db import models


class ArcweaveProject(models.Model):
    title = models.CharField(max_length=255, blank=True)
    json = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    zip_file = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.title


class AssetFile(models.Model):
    project = models.ForeignKey(ArcweaveProject, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='assets/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, blank=True)
