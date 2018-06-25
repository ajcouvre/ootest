from django.db import models
from django.conf import settings
from .file_validation import ValidFileField

# Create your models here.


class UploadFileModel(models.Model):
    upload = ValidFileField(
        upload_to='uploads/',
        content_types=['application/json'],
        max_upload_size=1024000
    )
    privacy = models.IntegerField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str(self):
        return self.upload_date

