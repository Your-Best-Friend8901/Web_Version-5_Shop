from django.shortcuts import render,redirect
from django.core.mail import send_mail
import random
from sito_web.models import Code_save,Products,Cart,Cart_Item,Category
from django.contrib.auth.models import User
from django.db.models import Sum,F,Count,Max,Min
from django.core.cache import cache
from django.contrib import messages
from router import router_cache

# {'head':{'Корзина':'Cart',
#                     'Аккаунт':'Account',
#                     'Гость':'Guest'},
def create_code(request):

    SESSION_ID = request.session.session_key
    
    KEY_CODE =f'code:{SESSION_ID}'
    TIMEOUT = 180 + random.randint(-20,20)

    cache_code = cache.get(KEY_CODE,None)


    KEY_USER_ID = f'cache_user_id:{request.session.session_key}'

    user_id =cache.get(KEY_USER_ID,None)

    if user_id is None:
        messages.warning(request,'Ваша сессия закончилось повторить Занова Авторизацию')
        raise ValueError() 

    elif cache_code is None:
        cache_code =random.randint(100000,999999)
        send_code(code=cache_code,id=user_id)
        cache.set(KEY_CODE,cache_code,TIMEOUT)

    else:
        messages.warning(request=request,message=f'Код уже был отправлен подождите {time}сек для следущего кода')        
    
    

def send_code(code,id):   
    try:
        user = User.objects.only('email').get(id=id)
        email = user.email
        subject ='Отправлен код '
        message = f'Ваш код {code}'
        from_email ='test@gmal.com'
        recipient_list =[email]
        send_mail(subject,message,from_email,recipient_list)
    except Exception as e:
        print(f'Error:{e}')



def func_delete_or_add_product(request,function,id_product):
    product =Products.objects.get(id=id_product)
    user = request.user

    cart, create = Cart.objects.get_or_create(user=user)
    item, create= Cart_Item.objects.get_or_create(cart=cart,product=product)


    if create is False:
        if function == 'add':
            item.quantity += 1
            item.save()
        elif function == 'delete':
            if item.quantity == 1:
                item.delete()
            else:
                item.quantity -= 1
                item.save()



    

def category_filter(category_name):
    KEY = str(category_name)
    TIMEOUT = 60 * 5 + random.randint(1,100)

    values = cache.get(KEY,None)

    if values is None:
        product_list = Products.objects.filter(category__name=category_name).values('name','price','id')
        values = list(product_list)
        cache.set(KEY,values,TIMEOUT)
        return values
    else:
        return values
    

def Sum_Price(user):
    Sum_product= Cart_Item.objects.filter(cart__user=user).select_related('product').only('product__name','product__price','quantity').annotate(
                Sum_product_price=F('product__price') * F('quantity'))
    
    
    Sum_products =Sum_product.aggregate(Sum_prices=Sum(F('product__price') * F('quantity')))

    return Sum_product,Sum_products

def count_product_category():
    router_cache()
    queryset_document = Category.objects.all().annotate(
                        number_products=Count('products'),
                        Max_price=Max('products__price'), 
                        Min_price=Min('products__price'))

    queryset_value= list(queryset_document.values())   
    return queryset_value

    
def get_random_products():
    TIME = 60 * 5
    KEY = 'get_random_products'

    products = cache.get( KEY,None)

    if products is None:
        queryset_document = Products.objects.order_by('?')[:5].values('id','price','imagin')
        queryset_value =list(queryset_document)
        cache.set(KEY,queryset_value,TIME)
        return queryset_value
    else:
        return products