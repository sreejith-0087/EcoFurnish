from django.urls import path
from . views import *


app_name = 'Cart'

urlpatterns = [
    path('', Cart_Details, name='cart'),
    path('add_cart/<int:product_id>', Add_Cart, name='add_cart'),
    path('full_remove/<int:product_id>', Full_Remove, name='full_remove'),
    path('cart_remove/<int:product_id>', Cart_Remove, name='cart_remove'),
    path('checkout/', Checkout, name='checkout'),
    path('placeorder/', PlaceOrder, name='placeorder'),
    path('card_payment/<int:order_id>', Card_Payment, name='card_payment'),
    path('order_view/', Order_View, name='order_view'),
]