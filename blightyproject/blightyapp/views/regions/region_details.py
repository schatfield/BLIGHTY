import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from blightyapp.models import Region, Pub


def get_region_pubs(region_id):

    return Pub.objects.filter(region_id=region_id)


# @login_required
def region_details(request, region_id):
    print("Its a poop balloon you bafoon")
    if request.method == 'GET':
        pubs = get_region_pubs(region_id)        
       

        template = 'regions/details.html'
        context = {
            'pubs': pubs
        }

        return render(request, template, context)