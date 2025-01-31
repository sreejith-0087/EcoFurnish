from django.shortcuts import render

# Create your views here.

def Cart(request):
    return render(request, 'Cart/Cart.html')