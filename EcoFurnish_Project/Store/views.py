from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request, 'Home/Index.html')

def About(request):
    return render(request, 'Home/About.html')

def Contact(request):
    return render(request, 'Home/Contact.html')