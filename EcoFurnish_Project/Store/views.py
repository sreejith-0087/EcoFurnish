from django.db.models.expressions import result
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q

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
        paginator = Paginator(all_items, 6)
        page_number = request.GET.get('page')
        products = paginator.get_page(page_number)

    return render(request, 'Store/Shop.html', {'products': products})


def Product_Search(request):
    query = request.GET.get('q')
    if query:
        result = Furniture.objects.all().filter(Q(product__icontains=query)|
                                                Q(category__category__icontains=query))
    else:
        result = []
    return render(request, 'Store/Shop.html', {'products': result})