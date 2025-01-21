from django.shortcuts import render, redirect

# Create your views here.

def Register(request):
    return render(request, 'Customer/Register.html')


def Login(request):
    return render(request, 'Customer/Login.html')