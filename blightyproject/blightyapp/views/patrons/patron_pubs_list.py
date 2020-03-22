import sqlite3
from django.shortcuts import redirect, render, reverse
from django.contrib.auth.decorators import login_required
from blightyapp.models import PatronPub, Pub


""" 

This view is what controls what happens when a user clicks wished/visited button on region_details form 

"""
@login_required
def patron_pub_list(request):

    print(request)

    if request.method == 'POST':        
        form_data = request.POST

        # [patron_pub_id] is the name in the form field and that is how it is getting the value. Since we are getting this value from the form we follow this pattern to declare the variable. it's just like the new_patron_pub variable below that is also getting the value for each key from the name we gave it in the form. Also, form_data is an object. it's holding all the request data from the form as an object and we are storing that object in the variable named form_data.
        patron_pub_id = form_data['patron_pub_id']
        # Getting region id off form, using it to redirect user to correct region page
        region_id = form_data['region_id']

        # this is saying if there is not a patron pub id present, post the request made by way of a form data object and construct it like this
        if not patron_pub_id:
            new_patron_pub = PatronPub(
                patron_id = request.user.patron.id,
                pub_id = form_data['pub_id'],
                is_wished = form_data['is_wished'],
                is_visited = form_data['is_visited'],
                has_experience = False, 
                beers_tried = "",
                food_ate = "",
                experience = ""
            )

            new_patron_pub.save()
            
        else: 
            
            patron_pub = PatronPub.objects.get(id=patron_pub_id)   
            
            # Which button was clicked, wished or visited?
            is_wished_button = form_data['is_wished'] == "True"
            
            if is_wished_button:
                patron_pub.is_wished = not patron_pub.is_wished 
            else:
                patron_pub.is_visited = not patron_pub.is_visited
            
            patron_pub.save()
                
            # Use context input field to determine where in the app the user click wished or visited buttons
            # the name on the form can be used as a property on form_data
        context = form_data['context']
        if context == 'wish_list':
            return redirect('blightyapp:wish_list')
        elif context == 'visited_list':
            return redirect('blightyapp:visited_list')
        else:
            return redirect('blightyapp:region_details', region_id=region_id)

    # """ 
    #         To do: assign the value of the patron_pub_id input field from the hidden form to a variable
    #         Conditionals
    #         First: we have to check if the value of patron_pub_id is none or some sort of empty string- print to see what is return to define this. 
    #         If it's empty, it is a post (nothing to PUT yet) - POST functionality is currently working
    #         Else we are gonna make a put - PUT needs to be written
        
    #     """


# zee shortcuts frauline:
# shift option command right arrow = multiple cursors down a list of stuff
# option jumps words
# holding shift highlights
# holding both highlights and jumps word


    

