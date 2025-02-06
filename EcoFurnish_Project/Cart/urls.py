from django.urls import path
from . views import *


app_name = 'Cart'

urlpatterns = [
    path('', Cart_Details, name='cart'),
    path('add_cart/<int:product_id>', Add_Cart, name='add_cart'),
    path('full_remove/<int:product_id>', Full_Remove, name='full_remove'),
    path('cart_remove/<int:product_id>', Cart_Remove, name='cart_remove'),
    path('checkout/', Checkout, name='checkout'),
]