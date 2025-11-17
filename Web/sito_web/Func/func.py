from django.shortcuts import render,redirect
from django.core.mail import send_mail
import random
from sito_web.models import Code_save,Products,Cart,Cart_Item
from django.contrib.auth.models import User


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
        product_list = Products.objects.filter(category=category_name)
    
        if len(product_list) == 0:
            return False
    
        return product_list
    except Exception as e:
        print(f'Error: {e}')

def Sum_price(cart_item):
    sum_price = 0
    product_price = []
    for i in cart_item:
        price =i.product.price * i.quantity
        product_price.append(price)
        sum_price += price
    return sum_price, product_price
