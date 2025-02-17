
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


@login_required(login_url='Customer:login')
def Full_Remove(request, product_id):
    cart = Cart.objects.get(user=request.user.id)
    product = get_object_or_404(Furniture, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('Cart:cart')


@login_required(login_url='Customer:login')
def Cart_Remove(request, product_id):
    cart = Cart.objects.get(user=request.user.id)
    product = get_object_or_404(Furniture, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('Cart:cart')



@login_required(login_url='Customer:login')
def Checkout(request, total=0, counter=0):
    user = CustomerDetails.objects.get(id=request.user.id)
    cart = Cart.objects.get(user=request.user.id)
    cart_item = CartItem.objects.filter(cart=cart, active=True)
    for i in cart_item:
        total =+ (i.product.price * i.quantity)
        counter += i.quantity
    return render(request, 'Cart/Checkout.html', {'cart_item':cart_item, 'total':total,
                                                  'user_details':user, 'cart_id':cart.id, 'counter': counter})



@login_required(login_url='Customer:login')
def PlaceOrder(request):
    if request.method == 'POST':
        add = request.POST['c_address']
        pin = request.POST['c_postal_zip']
        type = request.POST['payment_option']

        user_details = CustomerDetails.objects.get(id=request.user.id)
        cart = Cart.objects.get(user=request.user.id)

        total_amount = 0

        order = Order.objects.create(user=user_details,
                                     cart_id=cart,
                                     address=add,
                                     postal_zip=pin,
                                     payment_type=type,
                                     payment_status=False)
        order.save()

        cart_item = CartItem.objects.filter(cart=cart, active=True)
        for i in cart_item:
            product = i.product
            product.stock -= i.quantity
            product.save()

            total_amount += (product.price * i.quantity)

            ProductOrder.objects.create(order=order, product=product, quantity=i.quantity,
                                        product_total=product.price * i.quantity)

        order.amount = total_amount
        order.save()

        cart_item.delete()

        if type == '1':
            return render(request, 'Cart/Thankyou.html')
        else:
            return redirect('Cart:card_payment', order.id)
    return HttpResponseNotAllowed(['POST'])


@login_required(login_url='Customer:login')
def Card_Payment(request, order_id):
    if request.method == 'POST':
        card_number = request.POST.get('card_number')
        name = request.POST.get('card_name')
        expiry_month = request.POST.get('expiry_month')
        expiry_year = request.POST.get('expiry_year')
        cvv = request.POST.get('cvv')

        user_details = CustomerDetails.objects.get(id=request.user.id)
        order = Order.objects.get(id=order_id)

        pay = Payment(
            user=user_details,
            order=order,
            card_number=card_number,
            name=name,
            expiry_month=expiry_month,
            expiry_year=expiry_year,
            cvv=cvv
        )
        pay.save()
        order.payment_status = True
        order.save()

        return render(request, 'Cart/Thankyou.html')
    return render(request, 'Cart/Card_Payment.html')