from django.urls import path
from .views import *

app_name = "blightyapp"

urlpatterns = [
    # path('', pub_list, name='home'),
    # path('region/<:region_id>/pubs/', pub_list, name='pubs'),
    path('', region_list, name='home'),
    path('regions/<int:region_id>/', region_details, name='region')
]