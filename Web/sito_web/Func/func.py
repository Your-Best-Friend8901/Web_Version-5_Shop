from django.shortcuts import render,redirect
from django.core.mail import send_mail
import random
from sito_web.models import Code_save,Products,Cart,Cart_Item,Category
from django.contrib.auth.models import User
from django.db.models import Sum,F,Count,Max,Min


# {'head':{'Корзина':'Cart',
#                     'Аккаунт':'Account',
#                     'Гость':'Guest'},

def Create_code(request):
    code =random.randint(100000,999999)
    user_id = request.session.get('user_id',None)

    if user_id is None:
        raise ValueError
    
    Code_save.objects.create(user_id=user_id,code=code)

    Send_code(code=code,id=user_id)
    

def Send_code(code,id):
    try:
        user = User.objects.get(id=id)
        email = user.email
        subject ='Отправлен код '
        message = f'Ваш код {code}'
        from_email ='test@gmal.com'
        recipient_list =[email]
        send_mail(subject,message,from_email,recipient_list)
    except Exception as e:
        print(f'Error:{e}')


def Random_Product(request):
    products = Products.objects.order_by('?')[:5]
    

def Add_Delete_to_Cart(request,function,id_product):
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



    

def Category_filter(request,category_name):
    try:
        product_list = Products.objects.filter(category__name=category_name)
    
        if len(product_list) == 0:
            return False
    
        return product_list
    except Exception as e:
        print(f'Error: {e}')


def Sum_Price(user):
    Sum_product= Cart_Item.objects.filter(cart__user=user).select_related('product').only('product__name','product__price','quantity').annotate(
                Sum_product_price=F('product__price') * F('quantity'))
    
    
    Sum_products =Sum_product.aggregate(Sum_prices=Sum(F('product__price') * F('quantity')))

    return Sum_product,Sum_products

def CountProduct_Category():
    return  Category.objects.all().annotate(
            number_products=Count('products'),
            Max_price=Max('products__price'), 
            Min_price=Min('products__price'))
