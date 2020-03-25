import sqlite3
from django.shortcuts import redirect, render, reverse
from django.contrib.auth.decorators import login_required
from urllib.parse import urlparse
from blightyapp.models import PatronPub
from blightyapp.models import Pub

""" 
This view handles getting the experience form, posting the data entered into the form, Editing and Deleting of an Experience

"""


def get_patron_pub(patron_pub_id):    
    return PatronPub.objects.get(id=patron_pub_id)


@login_required
def experience_form(request, patron_pub_id):
    # this is getting the patron_pub record from the data and is available to the whole function
    patron_pub = get_patron_pub(patron_pub_id)   

    if request.method == 'GET':

        next_url = request.META.get('HTTP_REFERER')
        next_url = urlparse(next_url)
        next_url = next_url.path
        print(next_url)
        
        template = 'experiences/form.html'
        context = {
            'patron_pub': patron_pub,
            'next_url': next_url
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for deleting an experience
        #
        # Note: You can use parenthesis to break up complex
        #       `if` statements for higher readability
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            patron_pub.has_experience = False
            patron_pub.beers_tried = ""
            patron_pub.food_ate = ""
            patron_pub.experience = ""

            # saving updated patron_pub record with the updated experience as blank and as false
            patron_pub.save()

            return redirect(reverse('blightyapp:experience_list'))

@login_required
def experience_edit_form(request, patron_pub_id):  

    if request.method == 'GET':
        patron_pub = get_patron_pub(patron_pub_id)     
        print(patron_pub)

        template = 'experiences/form.html'
        context = {
            
            'patron_pub': patron_pub
        }

        return render(request, template, context)