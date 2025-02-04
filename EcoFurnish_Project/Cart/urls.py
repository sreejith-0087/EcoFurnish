from django.urls import path
from . views import *


app_name = 'Cart'

urlpatterns = [
    path('', Cart_Details, name='cart'),
    path('add_cart/<int:product_id>', Add_Cart, name='add_cart'),
]