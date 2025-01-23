from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import Categories, Furniture, Feedback
from Customer.models import CustomerDetails


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


def Single_Details(request, pro_id):
    ecofurnishsingle = Furniture.objects.get(id=pro_id)
    feedback_list = Feedback.objects.filter(product_id=pro_id).order_by('-created_at')
    return render(request, 'Store/Shop_Details.html', {'pro': ecofurnishsingle,
                                                       'feedback_view':feedback_list})


@login_required(login_url='Customer:login')
def Add_Feedback(request, pro_id):
    if request.method == 'POST':
        fed = request.POST['Add_Feedback']
        product = Furniture.objects.get(id=pro_id)
        user = CustomerDetails.objects.get(id=request.user.id)
        Feedback(user=user, feedback=fed, product=product).save()
        return redirect('Store:single_details', pro_id)



def Feedback_View(request, product_id):
    feedback_list = Feedback.objects.filter(product_id=product_id).order_by('-created_at')
    return render(request, 'Store/Shop_Details.html', {'feedback_view':feedback_list})



