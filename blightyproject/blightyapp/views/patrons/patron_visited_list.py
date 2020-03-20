import sqlite3
from django.shortcuts import redirect, render, reverse
from django.contrib.auth.decorators import login_required
from blightyapp.models import PatronPub, Pub


@login_required
def patron_visited(request):
    print('VISITED!')
    if request.method == 'GET':
        patron_id = request.user.patron.id
        visited_pubs = PatronPub.objects.filter(is_visited=True, patron_id=patron_id )
        template = 'patron_pubs/visited_list.html'
        context = {
            'visited_pubs': visited_pubs
        }
        
        return render(request, template, context)