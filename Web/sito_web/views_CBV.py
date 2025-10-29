from django.views.generic import FormView,View
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from sito_web.forms import RegistrationForm,CodeForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render,redirect
from sito_web.Func.func import Create_code
from sito_web.models import Code_save,Cart_Item




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
        if not request.user.is_autheticated:
            messages.warning(request,'Чтобы увидеть товар в корзине надо Авторизоватся в Аккаунт')      
            return render(request,'Main/Main.html')  
        cart_item = Cart_Item.objects.filter(cart__user=request.user)
        return render(request,'Cart/Cart.html',context={'cart_item': cart_item})

        


    
#class UniversalView()

