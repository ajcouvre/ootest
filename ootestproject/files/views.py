from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template import loader
from .forms import UploadForm
from .models import UploadFileModel
from django.conf import settings


def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = UploadFileModel(file_field=request.FILES['file'])
            instance.save()
            return HttpResponseRedirect('/success')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def upload_list(request):
    uploaded_files_list = UploadFileModel.objects.filter(author=settings.AUTH_USER_MODEL)
    template = loader.get_template('files/upload_list.html')
    context = {'uploaded_files_list': uploaded_files_list}
    return HttpResponse(template, context)
