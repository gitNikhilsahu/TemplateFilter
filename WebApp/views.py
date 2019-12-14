from django.shortcuts import render
from .models import FilterModel

def DataView(request):
    datalist = FilterModel.objects.all()
    return render(request, 'WebApp/Data.html', {'datalist':datalist})
    