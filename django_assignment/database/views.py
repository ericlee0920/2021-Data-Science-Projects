from django.shortcuts import render 
from django.http import HttpResponse

def download(request):
    return render(request, 'download.html')

def search(request):
    return render(request, 'search.html')

def upload(request):
    return render(request, 'upload.html')
