from django.shortcuts import render
from .Func.func import Router_Get
from .CBV import RegistrationView
# Create your views here.

def Main_Page(request):
    return Router_Get(request)

def Main_auth(request):
    return render(request,'Main_auth/Main_auth.html')

def Registration(request):
    return RegistrationView.as_view()(request)

def Login(request):
    pass