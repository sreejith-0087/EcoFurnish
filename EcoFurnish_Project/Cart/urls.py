from django.urls import path
from . views import *


app_name = 'Cart'

urlpatterns = [
    path('', Cart, name='cart'),
]