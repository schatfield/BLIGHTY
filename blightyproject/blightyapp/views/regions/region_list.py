import sqlite3
from django.shortcuts import render
from blightyapp.models import Region


def region_list(request):
    if request.method == 'GET':
        all_regions = Region.objects.all()
        template = 'regions/list.html'
        context = {
            'all_regions': all_regions
        }
        

        return render(request, template, context)