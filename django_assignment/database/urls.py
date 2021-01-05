from django.urls import path, include
from . import views

urlpatterns = [
    path('download/', views.download, name='download'),
    path('search/', views.search, name='search'),
    path('upload/', views.upload, name='upload'),
]