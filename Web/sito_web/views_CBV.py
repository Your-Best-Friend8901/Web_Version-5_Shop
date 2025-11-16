from django.views.generic import FormView,View,UpdateView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from sito_web.forms import RegistrationForm,CodeForm,ContextForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render,redirect
from sito_web.Func.func import Create_code,Sum_price
from sito_web.models import Code_save,Cart_Item,Profile_Context




class LoginView(FormView):
    template_name = 'Main_auth/Login/login1.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('Login2')

    def form_valid(self, form):

        user = form.get_user()
        self.request.session['user_id'] = user.id
        
        return super().form_valid(form)
    
    
class CodeView(View):
    def get(self,request):
        check_get = self.request.GET.get('send_code',None)
        form = CodeForm()
        try:

            if check_get is None:
                return render(request=self.request,template_name='Main_auth/Login/Verification_email.html',context={'form':form})
            
            Create_code(request=self.request)

            return render(request=self.request,template_name='Main_auth/Login/Verification_email.html',context={'form':form})
        
        except ValueError:

            return render(request=self.request,template_name='Main/Main.html',context={'error':'Что то пошло не так повторить Авторизацию'})
    
    def post(self,request):

        form = CodeForm(self.request.POST,request=self.request)

        if form.is_valid():
            user_id = self.request.session['user_id']
            user = User.objects.get(id=user_id)

            Code_save.objects.filter(user_id=user_id).delete()

            login(request=self.request, user=user)
            messages.success(request,'Вы прошли Авторизацию')
            return redirect('Main')
            
        else:
            return render(request=self.request,template_name='Main_auth/Login/Verification_email.html',context={'form':form})



class RegistrationView(FormView):
    template_name = 'Main_auth/Registration/Registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('Main')
    
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
        cart_item = Cart_Item.objects.select_related('product').filter(cart__user=request.user)
        sum_price,product_price = Sum_price(cart_item)
        request.session['Page'] = 'Cart'
        return render(request,'Cart/Cart.html',context={'cart_item': cart_item,
                                                        'sum_price': sum_price,
                                                        'product_price':product_price})

class Profile(View):
    def get(self,request):
        if not request.user.is_authenticated:
            messages.warning(request,'Чтобы Зайти в свой профиль надо Авторизаватся в Аккаунт ')      
            return render(request,'Main/Main.html')  
        
        profile_avatar,create =Profile_Context.objects.get_or_create(user= request.user)
        return render(request,'Profile/Profile.html',context={'profile_avatar':profile_avatar})


class Profile_edit_Succes(View):
    def get(self,request):
        
        profile_avatar,create =Profile_Context.objects.get_or_create(user= request.user)

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

