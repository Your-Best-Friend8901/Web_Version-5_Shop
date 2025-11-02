from django.shortcuts import render,redirect
from sito_web.Func.func import Router_Get,Add_to_Cart,Category_filter
from .views_CBV import RegistrationView,LoginView,CodeView,Cart
from django.contrib import messages
# Create your views here.

############### <Основная страница>
def Main_Page(request):
    return Router_Get(request)
############### <Основная страница/>

############### <Меню Авторизаций>
def Main_auth(request):
    return Router_Get(request)
############### <Меню Авторизаций/>

############### <Категория>
def Category(request):
    return render(request,'Category/Category.html')

######## Филитр продуктов
def Category_products(request,category_name):
    filter_result = Category_filter(request,category_name)

    if filter_result is False:
        messages.error(request,'В этой категорий еще нету продуктов')
        return render(request,'Category/Category.html')
    
    return render(request,'Category/Category_products.html',context={'products': filter_result})

######## Добавить Продукт
def Cart_add(request,id_product):
    if not request.user.is_authenticated:    
        messages.warning(request,'Чтобы добавить товар в корзину надо Авторизоватся в Аккаунт')
        return render(request,'Main/Main.html')
    
    Add_to_Cart(request,id_product)
    return redirect('Main')
######## Удалить Продукт
def Cart_delete(request,id_product):
    if not request.user.is_authenticated:    
        messages.warning(request,'Чтобы добавить товар в корзину надо Авторизоватся в Аккаунт')
        return render(request,'Main/Main.html')
    
    
############### <Категория/>
    
############### <Выход>
def Exit(request,Page):
    return redirect(Page)
############### <Выход/>
    
############### <Оплата>
def Buy_product(request):
    return render(request,'Buy_product/main.html')
############### <Оплата/.>
