from django.forms import ModelForm
from files.models import UploadFileModel


class UploadForm(ModelForm):
    class Meta:
        model = UploadFileModel
        fields = ['upload', 'privacy', 'author']
