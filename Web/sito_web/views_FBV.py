from django.shortcuts import render,redirect
from sito_web.Func.func import Router_Get,Add_to_Cart
from .views_CBV import RegistrationView,LoginView,CodeView,Cart
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

def Cart_Page(request):
    return Cart.as_view()(request)

def Cart_add(request,id_product):
    if not request.user.is_authenticated:    
        messages.warning(request,'Чтобы добавить товар в корзину надо Авторизоватся в Аккаунт')
        return render(request,'Main/Main.html')
    
    Add_to_Cart(request,id_product)
    

    
    
