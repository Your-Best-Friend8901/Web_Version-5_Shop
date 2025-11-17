from django.shortcuts import render,redirect
from sito_web.Func.func import Add_Delete_to_Cart,Category_filter
from .views_CBV import RegistrationView,LoginView,CodeView,Cart
from django.contrib import messages
from django.views.decorators.cache import cache_page
from .models import Products,Category
# Create your views here.

############### <Основная страница>
@cache_page(60*15)
def Main_Page(request):
    request.session['Page'] = 'Main'
    products = Products.objects.order_by('?')[:5]
    return render(request,'Main/Main.html',context={'product':products})
############### <Основная страница/>

############### <Меню Авторизаций>
def Main_auth(request):
    return render(request,'Main_auth/Main_auth.html')
############### <Меню Авторизаций/>

############### <Категория>
def Category_Page(request):
    Categorys = Category.objects.all()
    return render(request,'Category/Category.html',context={'Categorys':Categorys})

######## Филитр продуктов
def Category_products(request,category_name):
    filter_result = Category_filter(request,category_name)
    if filter_result is False:
        messages.error(request,'В этой категорий еще нету продуктов')
        return render(request,'Category/Category.html')
    return render(request,'Category/Category_products.html',context={'products': filter_result})

######## <Добавить/Удалить Продукт>
def Add_delete_product(request,function,id_product):
    ####### Проверка аутефикаиций
    if not request.user.is_authenticated:    
                messages.warning(request,'Чтобы добавить товар в корзину надо Авторизоватся в Аккаунт')
                return render(request,'Main/Main.html')
    direction = request.session['Page']
    ####### Сам процесс
    Add_Delete_to_Cart(request,function,id_product)
    return redirect(direction)
######## <Добавить/Удалить Продукт/>

############### <Категория/>
    
############### <Выход>
def Exit(request,Page):
    return redirect(Page)
############### <Выход/>
    
############### <Оплата>
def Buy_product(request):
    return render(request,'Buy_product/main.html')
############### <Оплата/.>
