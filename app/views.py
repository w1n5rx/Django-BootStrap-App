from django.shortcuts import render, HttpResponse
from app.models import Sites

# Create your views here.
def home(request):
    numbers = [1, 2, 3, 4, 5]
    name = 'Some name'


    args = {'name': name, 'numbers': numbers}
    return render(request, 'app/index.html', args)

def summary(request):
    return render(request, 'app/summary.html')

def summaryavg(request):
    return render(request, 'app/summary-average.html')

def sites(request, site_id):
    # data = Sites(date_value='2015-02-01', A_value=12.00, B_value=16.00, site_name='Demo Site')
    # data.save()
    Sites.objects.all().delete()

    # if Sites is None:
    data = Sites.objects.bulk_create([
        Sites(date_value='2015-02-01', A_value=12.00, B_value=16.00, site_name='Demo Site'),
        Sites(date_value='2015-02-03', A_value=20.00, B_value=100.00, site_name='Demo Site'),
        Sites(date_value='2015-02-10', A_value=20.00, B_value=80.00, site_name='Demo Site'),
        Sites(date_value='2015-02-03', A_value=5.00, B_value=15.00, site_name='ABC Site'),
        Sites(date_value='2015-02-15', A_value=5.00, B_value=15.00, site_name='XYZ Site'),
        Sites(date_value='2015-02-28', A_value=5.00, B_value=15.00, site_name='XYZ Site'),
    ])

    path = request.path_info.lstrip('/')
    print('path', path)

    args = {'sites': Sites.objects.filter(site_name='Demo Site'), 'site_name': Sites.objects.filter(site_name='Demo Site')[0].site_name}
    if path == 'sites/1/':
        args = {'sites': Sites.objects.filter(site_name='Demo Site'), 'site_name': Sites.objects.filter(site_name='Demo Site')[0].site_name}
    elif path == 'sites/2/':
        args = {'sites': Sites.objects.filter(site_name='ABC Site'), 'site_name': Sites.objects.filter(site_name='ABC Site')[0].site_name}
    elif path == 'sites/3/':
        args = {'sites': Sites.objects.filter(site_name='XYZ Site'), 'site_name': Sites.objects.filter(site_name='XYZ Site')[0].site_name}

    return render(request, 'app/sites/' +site_id+ '.html', args)
