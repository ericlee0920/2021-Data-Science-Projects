from django.shortcuts import render 
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import Sample
import csv, io

def download(request):
    template = 'download.html'

    return render(request, template)

def search(request):
    template = 'search.html'

    return render(request, template)


@permission_required('admin.can_add_log_entry')
def upload(request):
    template = 'upload.html'

    prompt = {
        'order': 'Order of the CSV should be sample_name, description, time'
    }

    if request.method == 'GET':
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request, "This is not a csv file")
    
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Sample.objects.update_or_create(
            sample_name=column[0],
            description=column[1]
        )

    context = {
        'samples': Sample.objects.all()
    }

    return render(request, template, context)
