from django.urls import path
from . import views

urlpatterns = [
    path('upload_file/', views.upload_file, name="upload_file"),
    path('upload_list/', views.upload_list, name="upload_list")
]
