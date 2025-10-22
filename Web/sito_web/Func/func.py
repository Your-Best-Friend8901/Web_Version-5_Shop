from django.shortcuts import render,redirect
from django.core.mail import send_mail
import random

def Router_Get(request):

    def Verification_Get(request):
        check_data = request.GET.get('Teleport',None)
        print("Все GET параметры:", dict(request.GET))
        
        if check_data is None:
            return render(request,'Main/Main.html',context={'check_data': check_data})
        
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

def Create_code():
    code =random.randint(100000,999999)
    

def Send_code(code,email):
     code =random.randint(100000,999999)
     subject ='Отправлен код '
     message = f'Ваш код {code}'
     from_email ='test@gmal.com'
     recipient_list =[]
     send_mail(subject,message,from_email,recipient_list)


