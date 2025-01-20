from django.urls import path
from . views import *


urlpatterns = [
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('shop/', Shop, name='shop'),
    path('category/<slug:link>', Shop, name='by_category'),
    path('product_search/', Product_Search, name='product_search'),
]

