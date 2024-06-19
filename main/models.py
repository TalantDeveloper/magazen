from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Magazen(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='image/')
    file = models.FileField(upload_to='jurnal/')
    content = RichTextUploadingField(verbose_name="Content")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

