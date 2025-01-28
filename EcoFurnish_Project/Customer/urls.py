from django.urls import path
from . views import *


app_name = 'Customer'

urlpatterns = [
    path('register/', Register, name='register'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('profile/', Profile, name='profile'),
    path('change-password/', Change_Password, name='change_password'),
]

