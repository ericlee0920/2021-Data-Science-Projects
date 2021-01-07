from django.urls import path, include
from . import views

urlpatterns = [
    path('download/', views.download, name='download'),
    path('download-csv/', views.sample_download, name='sample_download'),
    path('search/', views.search, name='search'),
    path('upload/', views.upload, name='upload'),
]