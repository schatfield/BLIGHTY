import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from blightyapp.models import Region, Pub, PatronPub


def get_region_pubs(region_id):

    return Pub.objects.all().filter(region_id=region_id).prefetch_related()


# @login_required
def region_details(request, region_id):
    if request.method == 'GET':
        pubs = get_region_pubs(region_id) 
        patron_id = request.user.patron.id
        for pub in pubs:
            patron_pub = PatronPub.objects.filter(pub_id=pub.id, patron_id=patron_id)             
            
            if len(patron_pub) == 0:
                pub.patron_pub = None
            else:
                pub.patron_pub = patron_pub[0]

        template = 'regions/details.html'
        context = {
            'pubs': pubs
        }

        return render(request, template, context)