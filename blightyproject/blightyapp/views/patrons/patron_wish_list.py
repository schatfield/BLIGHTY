import sqlite3
from django.shortcuts import redirect, render, reverse
from blightyapp.models import PatronPub, Pub



def patron_wished(request):
    print("WISHED!!!")
    if request.method == 'GET':
        patron_id = request.user.patron.id
        wished_pubs = PatronPub.objects.filter(is_wished=True, patron_id=patron_id )
        template = 'patron_pubs/wish_list.html'
        context = {
            'wished_pubs': wished_pubs
        }
        
        return render(request, template, context)