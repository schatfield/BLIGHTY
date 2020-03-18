import sqlite3
from django.shortcuts import redirect, render, reverse
from blightyapp.models import PatronPub, Pub


def experience_list(request):
    if request.method == 'POST':        
        form_data = request.POST

        # experience = form_data['beers']
        # print('experience!!!!',experience)

        # Todo: Get patron pub id off form - why
        # Todo: Get patron pub record using patron pub id- why
        # Todo: Update properties on patron pub records using form data, and set has_experience to true- how 
        # Todo: .save()

        # Get patron pub id off form - need the id to make sure we are getting the user specific record to update 
        patron_pub_id = form_data['patron_pub_id']
        print('PATRONPUBIDDDDDD', patron_pub_id)
        # Get patron pub record using patron pub id- need to uodate the user specific record with the new experience
        patron_pub = PatronPub.objects.get(id=patron_pub_id) 
        # Update properties on patron pub records using form data, and set has_experience to true- so now we have tracked that they've added an experience
        patron_pub.has_experience = True
        patron_pub.beers_tried = form_data['beers']
        patron_pub.food_ate = form_data['food']
        patron_pub.experience = form_data['experience']
        
        # saving updated patron_pub record with the added experience
        patron_pub.save()
        
        return redirect(reverse('blightyapp:home'))


        # add_experience_button = form_data['experience'] == "True"