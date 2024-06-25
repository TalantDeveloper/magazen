# Generated by Django 5.0.6 on 2024-06-25 04:08

import ckeditor_uploader.fields
import main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('author', models.CharField(max_length=255, verbose_name='author')),
                ('image', models.ImageField(default='image/image.jpg', upload_to='image/')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Content')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='magazen',
            name='file',
            field=models.FileField(upload_to=main.models.upload_to),
        ),
        migrations.AlterField(
            model_name='magazen',
            name='image',
            field=models.ImageField(blank=True, default='/media/image/logotip.ico', null=True, upload_to=main.models.upload_to),
        ),
    ]
