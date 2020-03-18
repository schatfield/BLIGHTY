from django.urls import path
from .views import *
from django.urls import include, path



app_name = "blightyapp"

urlpatterns = [
    # path('', pub_list, name='home'),
    # path('region/<:region_id>/pubs/', pub_list, name='pubs'),
    path('regions/', region_list, name='home'),
    path('regions/<int:region_id>/', region_details, name='region'),
    path('experiences/<int:patron_pub_id>/', experience_form, name='experience_form'),
    path('patron_pub/', patron_pub_list, name='patron_pub_list'),
    #     Added a route for gettting the register form and submitting register form data
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register_user, name="register"),
    path('logout/', logout_user, name='logout'),
]