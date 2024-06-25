from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

import os
from datetime import datetime


def upload_to(instance, filename):
    # Get current date
    now = datetime.now()
    # Define the upload path
    year_month = now.strftime('%Y-%m')  # Format: YYYY-MM

    # Modify filename (example: adding timestamp)
    filename_without_ext, ext = os.path.splitext(filename)
    timestamp = now.strftime('%Y%m%d%H%M%S')
    new_filename = f"{timestamp}{ext}"

    return os.path.join('uploads', year_month, new_filename)


class Category(models.Model):
    name = models.CharField(verbose_name='category', max_length=50)

    def __str__(self):
        return self.name


class Magazen(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to=upload_to, default="/media/image/logotip.ico", null=True, blank=True)
    file = models.FileField(upload_to=upload_to)
    content = RichTextUploadingField(verbose_name="Content")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Announcement(models.Model):
    name = models.CharField(max_length=255, verbose_name="name")
    author = models.CharField(max_length=255, verbose_name="author")
    image = models.ImageField(upload_to='image/', default='image/image.jpg')
    content = RichTextUploadingField(verbose_name="Content")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


