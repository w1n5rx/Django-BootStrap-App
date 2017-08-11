from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    numbers = [1, 2, 3, 4, 5]
    name = 'Some name'

    args = {'name': name, 'numbers': numbers}
    return render(request, 'app/index.html', args)

def summary(request):
    return render(request, 'app/summary.html')

def first(request):
    return render(request, 'app/first.html')

# def summary-avg(request):
#     return render(request, 'app/summary-average.html')