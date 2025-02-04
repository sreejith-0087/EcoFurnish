from django.shortcuts import render, redirect, get_object_or_404
from Customer.models import CustomerDetails
from Store.models import Furniture
from .models import *
from django.http import HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

@login_required(login_url='Customer:login')
def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


@login_required(login_url='Customer:login')
def Add_Cart(request, product_id):
    user = CustomerDetails.objects.get(id=request.user.id)
    product = Furniture.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(user=request.user.id)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request), user=user)
        cart.save()

    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity +=1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )
        cart_item.save()

    return redirect("Cart:cart")



@login_required(login_url='Customer:login')
def Cart_Details(request, total=0, counter=0, cart_items=0):
    try:
        cart = Cart.objects.get(user=request.user.id)
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for i in cart_items:
            total += (i.product.price * i.quantity)
            counter += i.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'Cart/Cart.html', dict(cart_items=cart_items, total=total, counter=counter))











