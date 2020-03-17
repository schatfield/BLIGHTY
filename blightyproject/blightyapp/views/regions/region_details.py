import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
from blightyapp.models import Region, Pub, PatronPub


def get_region_pubs(region_id):

    return Pub.objects.all().filter(region_id=region_id).prefetch_related()


# @login_required
def region_details(request, region_id):

    """ This function GETs pubs by region (region_details) and loops through each pub """

    if request.method == 'GET':
        pubs = get_region_pubs(region_id) 
        patron_id = request.user.patron.id
        for pub in pubs:
            """ This line is making a call to get the PatronPub record in the data for the pub with filter method (filter is like saying "where") """

            patron_pub = PatronPub.objects.filter(pub_id=pub.id, patron_id=patron_id)             
            
            """ We are going to add a new Patron Pub Property on every Pub """
            """ This is checking for a the Patron Pub record - if there's no record (i.e. "0") set new property to "None" """

            if len(patron_pub) == 0:
                pub.patron_pub = None

            """ If there is a record present, assign the patron_pub record to the patron_pub property (attaching the patron pub record to the pub. this is the record you created above: PatronPub.objects.filter(pub_id=pub.id, patron_id=patron_id)  using bracket notation because the ORM is returning a list )"""

            else:
                pub.patron_pub = patron_pub[0]

        template = 'regions/details.html'
        context = {
            'pubs': pubs
        }

        return render(request, template, context)