from django.urls import path
from . views import *


app_name = 'Customer'

urlpatterns = [
    path('register/', Register, name='register'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout')
]

