import sqlite3
from django.shortcuts import redirect, render, reverse
from django.contrib.auth.decorators import login_required
from blightyapp.models import PatronPub, Pub

@login_required
def experience_list(request):
    if request.method == 'POST':        
        form_data = request.POST

        # testing to see if we are getting anything in the terminal
        # experience = form_data['beers']
        # print('experience!!!!', experience)
        #Order of OPS:
        # Todo: Get patron pub id off form - why
        # Todo: Get patron pub record using patron pub id- why
        # Todo: Update properties on patron pub records using form data, and set has_experience to true- how 
        # Todo: .save()

        # Get patron pub id off form - need the id to make sure we are getting the user specific record to update 
        patron_pub_id = form_data['patron_pub_id']

        # Get patron pub record using patron pub id- need to uodate the user specific record with the new experience
        patron_pub = PatronPub.objects.get(id=patron_pub_id) 

        # Update properties on patron pub records using form data, and set has_experience to true- now we have tracked that they've added an experience and captured the values input to the form
        patron_pub.has_experience = True
        patron_pub.beers_tried = form_data['beers']
        patron_pub.food_ate = form_data['food']
        patron_pub.experience = form_data['experience']
        
        # saving updated patron_pub record with the added experience
        patron_pub.save()

        return redirect(reverse('blightyapp:home'))

    elif request.method == 'GET':
        patron_id = request.user.patron.id
        all_experiences = PatronPub.objects.filter(has_experience=True, patron_id=patron_id )
        template = 'experiences/list.html'
        context = {
            'all_experiences': all_experiences
        }
        
        return render(request, template, context)
       



