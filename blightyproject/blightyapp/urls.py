from django.urls import path
from .views import *

app_name = "blightyapp"

urlpatterns = [
    path('', pub_list, name='home'),
    path('pubs/', pub_list, name='pubs'),
]