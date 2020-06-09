from django.urls import path
from .views import *
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static



app_name = "blightyapp"

urlpatterns = [
    path('', home, name='home'),
    path('regions/', region_list, name='region_list'),
    path('regions/<int:region_id>/', region_details, name='region_details'),
    path('experiences/', experience_list, name='experience_list'),
    path('experiences/<int:patron_pub_id>/form/', experience_form, name='experience_form'),
    path('experiences/<int:patron_pub_id>/form/', experience_edit_form, name='experience_edit_form'),
    path('patron_pub/', patron_pub_list, name='patron_pub_list'),
    path('wishlist/', patron_wished, name='wish_list'),
    path('visited/', patron_visited, name='visited_list'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register_user, name='register'),
    path('logout/', logout_user, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)