from django.shortcuts import render, HttpResponse 
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from .models import Sample
import csv, io

@permission_required('admin.can_add_log_entry')
def sample_download(request):
    samples = Sample.objects.all()

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="sample.csv"'

    writer = csv.writer(response, delimiter=',')
    writer.writerow(['sample_name', 'description', 'time'])

    for sample in samples:
        writer.writerow([sample.sample_name, sample.description, sample.time])

    return response
    

def download(request):
    template = 'download.html'

    return render(request, template)

def search(request):
    template = 'search.html'

    return render(request, template)


@permission_required('admin.can_add_log_entry')
def upload(request):
    template = 'upload.html'

    samples = Sample.objects.all()

    context = {
        'samples': samples
    }

    if request.method == 'GET':
        return render(request, template, context)

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
    
    return render(request, template, context)
