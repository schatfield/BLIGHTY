import sqlite3
from django.shortcuts import redirect, render, reverse
from blightyapp.models import PatronPub, Pub


""" 

This view is what controls what happens when a user clicks wished/visited on region_details form 

"""

def patron_pub_list(request):
    if request.method == 'GET':
        
        all_pubs = Pub.objects.all()

        # title = request.GET.get('title', None)

        # if title is not None:
        #     all_books = all_books.filter(title__contains=title)

        # template = 'books/list.html'
        # context = {
        #     'all_books': all_books
        # }

        # return render(request, template, context)
    elif request.method == 'POST':        
        form_data = request.POST
        
        """ 
            To do: assign the value of the patron_pub_id input field from the hidden form to a variable
            Conditionals
            First: we have to check if the value of patron_pub_id is none or some sort of empty string- print to see what is return to define this. 
            If it's empty, it is a post (nothing to PUT yet) - POST functionality is currently working
            Else we are gonna make a put - PUT needs to be written
        
        """
        # instantiate...
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
       
    return redirect(reverse('blightyapp:home'))

# zee shortcuts frauline:
# shift option command right arrow = multiple cursors down a list of stuff
# option jumps words
# holding shift highlights
# holding both highlights and jumps word


    


        # and then save to the db
        # print(new_book.librarian.user.username) = prints user username

        # Or...
        # Use a shortcut to do both at the same time
        # new_book = Book.objects.create(
        #     title = form_data['title'],
        #     author = form_data['author'],
        #     isbn = form_data['isbn'],
        #     year = form_data['year_published'],
        #     location_id = request.user.librarian.id,
        #     librarian_id = form_data["location"]
        # )
