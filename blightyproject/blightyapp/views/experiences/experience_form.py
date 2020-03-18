import sqlite3
from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
from blightyapp.models import PatronPub
from blightyapp.models import Pub


def get_patron_pub(patron_pub_id):    
    return PatronPub.objects.get(id=patron_pub_id)


# @login_required
def experience_form(request, patron_pub_id):
    if request.method == 'GET':
        patron_pub = get_patron_pub(patron_pub_id)        
        
        template = 'experiences/form.html'
        context = {
            'patron_pub': patron_pub
        }

        return render(request, template, context)

# @login_required
# def book_edit_form(request, book_id):    

#     if request.method == 'GET':
#         book = get_book(book_id)
#         print(book)
#         libraries = get_libraries()

#         template = 'books/form.html'
#         context = {
#             'book': book,
#             'all_libraries': libraries
#         }

#         return render(request, template, context)