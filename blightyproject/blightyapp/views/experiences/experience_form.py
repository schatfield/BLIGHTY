import sqlite3
from django.shortcuts import redirect, render, reverse
from django.contrib.auth.decorators import login_required
from blightyapp.models import PatronPub
from blightyapp.models import Pub


def get_patron_pub(patron_pub_id):    
    return PatronPub.objects.get(id=patron_pub_id)


@login_required
def experience_form(request, patron_pub_id):
    # this is getting the patron_pub record form the data and is available to the whole function
    patron_pub = get_patron_pub(patron_pub_id)   

    if request.method == 'GET':
        
        template = 'experiences/form.html'
        context = {
            'patron_pub': patron_pub
        }

        return render(request, template, context)

    elif request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for deleting a book
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

            # saving updated patron_pub record with the added experience
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