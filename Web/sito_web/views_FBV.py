from django.shortcuts import render,redirect
from sito_web.Func.func import func_delete_or_add_product,category_filter,count_product_category,get_random_products
from sito_web.Func import func
from .views_CBV import RegistrationView,CodeView,Cart
from django.contrib import messages
from django.views.decorators.cache import cache_page
from .models import Products,Category
# Create your views here.

############### <Основная страница>
def main_page(request):
    request.session['Page'] = 'main'
    random_products = func.get_random_products()
    return render(request,'Main/main.html',context={'random_products':random_products})
############### <Основная страница/>

############### <Меню Авторизаций>
@cache_page(60*60)
def main_auth(request):
    return render(request,'main_auth/main_auth.html')
############### <Меню Авторизаций/>

############### <Категория>
def category_page(request):
    categories = func.count_product_category()
    return render(request,'Category/category.html',context={'categories':categories})

######## Филитр продуктов
def category_products(request,category_name):
    products = func.category_filter(category_name)
    return render(request,'Category/сategory_products.html',context={'products': products})

######## <Добавить/Удалить Продукт>
def delete_or_add_product(request,function,id_product):
    ####### Проверка аутефикаиций
    if not request.user.is_authenticated:    
                messages.warning(request,'Чтобы добавить товар в корзину надо Авторизоватся в Аккаунт')
                return render(request,'Main/main.html')
    direction = request.session['Page']
    ####### Сам процесс
    func.func_delete_or_add_product(request,function,id_product)
    return redirect(direction)
######## <Добавить/Удалить Продукт/>

############### <Категория/>

############### <Отправка кода>
def send_code_to_email(request):
    try:
        func.create_code(request)

        return redirect('login2')
            
    except ValueError:
        messages.error(request,'Произошла ошибка повторить отправку кода')
        return redirect('login2')
############### <Отправка кода/>

############### <Выход>
def exit(request,Page):
    return redirect(Page)
############### <Выход/>
    
############### <Оплата>
def buy_product(request):
    return render(request,'Buy_product/main.html')
############### <Оплата/.>
