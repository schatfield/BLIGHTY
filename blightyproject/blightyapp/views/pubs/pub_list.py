import sqlite3
from django.shortcuts import render
from blightyapp.models import Pub


def pub_list(request):
    if request.method == 'GET':
        all_pubs = Pub.objects.all()
        template = 'pubs/list.html'
        context = {
            'all_pubs': all_pubs
        }

        return render(request, template, context)