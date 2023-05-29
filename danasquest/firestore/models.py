from django.db import models


class Arcweave(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    project_settings = models.FileField(upload_to='project_json', null=True, blank=True)
    pic_cover = models.ImageField(upload_to='pic', null=True, blank=True)
    pic_characters = models.FileField(upload_to='pic', null=True, blank=True)
    pic_backgrounds = models.FileField(upload_to='pic', null=True, blank=True)

    class Meta:
        managed = True
        verbose_name = "Arcweave"
        verbose_name_plural = "Arcweave"
