from django.shortcuts import render, HttpResponse
from app.models import Sites
from django.db.models import Sum
from django.db import connection

# Create your views here.
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
def home(request):
    return render(request, 'app/index.html')

def summary(request):
    args = {'sites': [{'site_name':'Demo Site', 
                        'A_value': (Sites.objects.filter(site_name='Demo Site').aggregate(Sum('A_value')))['A_value__sum'], 
                        'B_value': (Sites.objects.filter(site_name='Demo Site').aggregate(Sum('B_value')))['B_value__sum']},
                    {'site_name':'ABC Site',                         
                        'A_value': (Sites.objects.filter(site_name='ABC Site').aggregate(Sum('A_value')))['A_value__sum'], 
                        'B_value': (Sites.objects.filter(site_name='ABC Site').aggregate(Sum('B_value')))['B_value__sum']},
                    {'site_name':'XYZ Site',                         
                        'A_value': (Sites.objects.filter(site_name='XYZ Site').aggregate(Sum('A_value')))['A_value__sum'], 
                        'B_value': (Sites.objects.filter(site_name='XYZ Site').aggregate(Sum('B_value')))['B_value__sum']}]}
    return render(request, 'app/summary.html', args)

def summaryavg(request):
    try:
        # Calculate average for Demo Site
        cursor = connection.cursor()
        cursor.execute('SELECT ROUND(AVG(A_value), 2) FROM app_sites where site_name="Demo Site"')
        a_val_demo = cursor.fetchone()
        cursor.execute('SELECT ROUND(AVG(B_value), 2) FROM app_sites where site_name="Demo Site"')
        b_val_demo = cursor.fetchone()

        # Calculate average for ABC Site
        cursor.execute('SELECT AVG(A_value) FROM app_sites where site_name="ABC Site"')
        a_val_abc = cursor.fetchone()
        cursor.execute('SELECT ROUND(AVG(B_value), 2) FROM app_sites where site_name="ABC Site"')
        b_val_abc = cursor.fetchone()

        # Calculate average for XYZ Site
        cursor.execute('SELECT ROUND(AVG(A_value), 2) FROM app_sites where site_name="XYZ Site"')
        a_val_xyz = cursor.fetchone()
        cursor.execute('SELECT ROUND(AVG(B_value), 2) FROM app_sites where site_name="XYZ Site"')
        b_val_xyz = cursor.fetchone()

        args = {'sites': [{'site_name':'Demo Site', 
                            'A_value': a_val_demo[0], 
                            'B_value': b_val_demo[0]},
                        {'site_name':'ABC Site', 
                            'A_value': a_val_abc[0], 
                            'B_value': b_val_abc[0]},
                        {'site_name':'XYZ Site', 
                            'A_value': a_val_xyz[0], 
                            'B_value': a_val_xyz[0]}
                        ]
                }
        return render(request, 'app/summary-average.html', args)
    except Exception as e:
        raise
    else:
        pass
    finally:
        cursor.close()



def sites(request, site_id):
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
