from itertools import product

from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from unicodedata import category

from . models import Categories, Furniture

# Create your views here.

def Home(request):
    return render(request, 'Home/Index.html')

def About(request):
    return render(request, 'Home/About.html')

def Contact(request):
    return render(request, 'Home/Contact.html')

def Shop(request, link=None):
    if link is not None:
        cat = Categories.objects.get(link=link)
        products = Furniture.objects.filter(category=cat.id)
    else:
        all_items = Furniture.objects.all()
        paginator = Paginator(all_items, 40)
        page_number = request.GET.get('page')
        products = paginator.get_page(page_number)

    return render(request, 'Store/Shop.html', {'products': products})


