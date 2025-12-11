from django.views.generic import FormView,View,UpdateView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from sito_web.forms import RegistrationForm,CodeForm,ContextForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render,redirect
from sito_web.Func.func import Sum_Price
from sito_web.models import Code_save,Cart_Item,Profile_Context
from sito_web.Func import func
from django.core.cache import cache
import random




class Login_view(FormView):
    template_name = 'Main_auth/Login/login1.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('login2')

    def form_valid(self, form):
        user = form.get_user().id
        KEY = f'cache_user_id:{self.request.session.session_key}'
        TIME = 160 + random.randint(0,20)

        user_id =cache.get(KEY,None)

        if user_id is None:
            cache.set(KEY,user,TIME)
            messages.success(self.request,'Вы прошли 1часть Авторизаций у вас есть 3минуты чтобы закончить 2часть для Входа в Аккаунт')
        
        return super().form_valid(form)
    
    
class CodeView(FormView):
    template_name = 'Main_auth/Login/verification_email.html'
    form_class = CodeForm
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        try:
            KEY = f'cache_user_id:{self.request.session.session_key}'
            user_id = cache.get(KEY,None)

            user = User.objects.get(id=user_id)
            login(request=self.request, user=user)

        except Exception:
            messages.error('Сессия истека повторите попытку')
            redirect('login')

        messages.success(self.request,'Вы прошли Авторизацию')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(request=self.request,message='Ваш код не подходит')
        return super().form_invalid(form)


class RegistrationView(FormView):
    template_name = 'Main_auth/Registration/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        User.objects.create_user(username=username,password=password,email=email)
        messages.success(request=self.request,message='Вы прошли Регистрацию теперь за Логинтесь')
        return super().form_valid(form)
     
class Cart(View):
    def get(self,request):
        if not request.user.is_authenticated:
            messages.warning(request,'Чтобы увидеть товар в корзине надо Авторизоватся в Аккаунт')      
            return render(request,'Main/Main.html')  
        product_price,sum_products = Sum_Price(user = request.user)
        request.session['Page'] = 'Cart'
        return render(request,'Cart/Cart.html',context={'products': product_price,
                                                        'Sum_products': sum_products})

class Profile(View):
    def get(self,request):
        if not request.user.is_authenticated:
            messages.warning(request,'Чтобы Зайти в свой профиль надо Авторизаватся в Аккаунт ')      
            return render(request,'Main/Main.html')  
        
        KEY = f'profile:{request.user.id}'
        TIMEOUT = 60000 + random.randint(1,1000)
        
        data_profile = cache.get(KEY,None)
        
        if data_profile is None:
            object,create =Profile_Context.objects.select_related('user').get_or_create(user= request.user)
            data_profile_dict = {
                'user__first_name': object.user.first_name,
                'user__last_name':object.user.last_name,
                'context':object.context,
                'ava': object.ava
                }
            cache.set(KEY,data_profile_dict,TIMEOUT)
            return render(request,'Profile/Profile.html',context={'profile_data':data_profile_dict})

        return render(request,'Profile/Profile.html',context={'profile_data':data_profile})


class Profile_edit(View):
    def get(self,request):
        
        KEY = f'profile:{request.user.id}'

        data_profile = cache.get(KEY,None)

        if data_profile is None:
            messages.warning(request,'Повторите попытку ваш кеш истек')
            redirect('profile')

        return render(request,'Profile/Profile.html',context={'Form': ContextForm,
                                                              'profile_avatar2':data_profile})
    
    def post(self,request):
        Form = ContextForm(request.POST,request.FILES)
        if Form.is_valid():
            first_name=Form.cleaned_data['first_name']
            last_name=Form.cleaned_data['last_name']
            context=Form.cleaned_data['context']
            ava = Form.cleaned_data['ava']

            context_user = Profile_Context.objects.get(user=request.user)
            user = request.user

            user.first_name = first_name
            user.last_name = last_name

            context_user.ava = ava
            context_user.context = context

            context_user.save()
            user.save()

            messages.success(request,'Профиль был изминен')

            return redirect('Profile')

        else:
            messages.error(request,'Не получилось изменить Профиль')

            return redirect('Profile')
            

# Будещий вариант для изминения профиля 
#class Profile_edit_context(UpdateView):
#    form_class = ''
#    template_name = ''
#    model = ''
#    success_url = ''


#class UniversalView()

