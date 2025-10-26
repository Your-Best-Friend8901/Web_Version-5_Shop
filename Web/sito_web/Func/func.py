from django.shortcuts import render,redirect
from django.core.mail import send_mail
import random
from sito_web.models import Code_save,Products
from django.contrib.auth.models import User


def Router_Get(request):

    def Verification_Get(request):
        check_data = request.GET.get('Teleport',None)
        print("Все GET параметры:", dict(request.GET))
        
        if check_data is None:
            products = Products.objects.order_by('?')[:5]
            return render(request,'Main/Main.html',context={'check_data': check_data,
                                                            'products' : products})
        
        return Search_in_dicts(request,value=check_data)


    def Search_in_dicts(request,value):
        dicts = {'category':{'context':{'category'}},
                 'Cart':{'template':'Cart/Cart.html'},
                 'Account':{'template':'Profile/Profile.html'},
                 'Menu_auth':{'template':'Main_auth/Main_auth.html'}}

        Position_dict = dicts.get(value)
        if value == 'category':
            Position_object = Position_dict.get('context')
        else:
            Position_object = Position_dict.get('template')

        return Render_Page(request,keys= Position_object)
        

    def Render_Page(request,keys):

        if type(keys) == dict:
            return render(request,'Main/Main.html',context=keys)
        
        return render(request,keys)
       
    return Verification_Get(request)
    

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
    

    