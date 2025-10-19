from django.views.generic import FormView,View
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from .forms import RegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages




class LoginView(FormView):
    template_name = 'Main_auth/Login/login1.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('Login2')

    def form_valid(self, form):

        user = form.get_user()
        self.request.session['user_id'] = user.id
        
        return super().form_valid(form)
    

class CodeView(View):
    template_name = 'Main_auth/Login/login2.html'
    

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
    


    
#class UniversalView()

