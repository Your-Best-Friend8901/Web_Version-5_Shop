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




class Login_view(FormView):
    template_name = 'Main_auth/Login/login1.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('login2')

    def form_valid(self, form):

        user = form.get_user()
        self.request.session['user_id'] = user.id
        
        return super().form_valid(form)
    
    
class CodeView(FormView):
    template_name = 'Main_auth/Login/verification_email.html'
    form_class = CodeForm
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        user_id = self.request.session['user_id']
        user = User.objects.get(id=user_id)

        Code_save.objects.filter(user_id=user_id).delete()

        login(request=self.request, user=user)
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
        
        profile_data,create =Profile_Context.objects.get_or_create(user= request.user)
        return render(request,'Profile/Profile.html',context={'profile_data':profile_data})


class Profile_edit(View):
    def get(self,request):
        
        profile_avatar,create =Profile_Context.objects.select_related('user').get_or_create(user= request.user)

        return render(request,'Profile/Profile.html',context={'Form': ContextForm,
                                                              'profile_avatar2':profile_avatar})
    
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

