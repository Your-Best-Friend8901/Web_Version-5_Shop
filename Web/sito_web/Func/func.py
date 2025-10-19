from django.shortcuts import render,redirect
from django.core.mail import send_mail
import random
def Router_Get(request):
    check_data = request.GET.get('Телепорт',None)
    print("Все GET параметры:", dict(request.GET))
    
    if check_data is None:
        return render(request,'Main/Main.html',context={'check_data': check_data})

    dicts = {'head':{'Регистрация':'Main_auth/Main_auth.html',
                     'Аккаунт': 'Profile/Profile.html',
                     'Корзина': ''},

        'category':{'Молочное':'Dairy products',
                        'Мясо':'Meat'}}
    
    abc = str(check_data).split()
    Position_dict = abc[0]
    Position_object = abc[1]

    Find_dict = dicts.get(Position_dict)
    Find_object = Find_dict.get(Position_object)

    if Position_dict == 'head':
        return render(request,Find_object)
    elif Position_dict =='category':
        return render(request,'Main/Main.html',context={'check_data': Find_object})

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


