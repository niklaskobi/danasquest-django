# Generated by Django 4.0.8 on 2023-01-14 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firestore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arcweave',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='arcweave',
            name='pic_backgrounds',
            field=models.FileField(blank=True, null=True, upload_to='pic'),
        ),
        migrations.AlterField(
            model_name='arcweave',
            name='pic_characters',
            field=models.FileField(blank=True, null=True, upload_to='pic'),
        ),
        migrations.AlterField(
            model_name='arcweave',
            name='pic_cover',
            field=models.ImageField(blank=True, null=True, upload_to='pic'),
        ),
        migrations.AlterField(
            model_name='arcweave',
            name='project_settings',
            field=models.FileField(blank=True, null=True, upload_to='project_json'),
        ),
    ]
