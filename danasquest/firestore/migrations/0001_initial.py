# Generated by Django 4.0.8 on 2023-01-13 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arcweave',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('project_settings', models.FileField(upload_to='project_json')),
                ('pic_cover', models.ImageField(upload_to='pic')),
                ('pic_characters', models.FileField(upload_to='pic')),
                ('pic_backgrounds', models.FileField(upload_to='pic')),
            ],
            options={
                'verbose_name': 'Arcweave',
                'verbose_name_plural': 'Arcweave',
                'managed': True,
            },
        ),
    ]
