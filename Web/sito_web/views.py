from django.shortcuts import render
from .Func.func import Router_Get
from .CBV import RegistrationView,LoginView,CodeView
from django.contrib import messages
# Create your views here.

def Main_Page(request):
    return Router_Get(request)

def Main_auth(request):
    return Router_Get(request)

def Registration(request):
    return RegistrationView.as_view()(request)

def Login(request):
    return LoginView.as_view()(request)

def Verificate_Email(request):
    return CodeView.as_view()(request)

def Category(request):
    pass

def Cart(request):
    pass

def Cart_add(request,id_product):
    if not request.user.is_authenticated:    
        messages.warning(request,'Чтобы добавить товар в корзину надо Авторизоватся в Аккаунт')
    
    user = request.user
