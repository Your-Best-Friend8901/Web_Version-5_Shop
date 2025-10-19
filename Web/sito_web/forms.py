from django import forms
from django.forms import ValidationError
from django.contrib.auth.models import User

class CodeForm(forms.Form):
    code = forms.CharField(max_length=7, widget=forms.TextInput)

    def clean(self):
        cleaned_data =  super().clean()
        try:
            code = cleaned_data['code']
            pass
        except:
            pass

class RegistrationForm(forms.Form):
    username=forms.CharField(min_length=3,max_length=16, widget=forms.TextInput)
    password=forms.CharField(min_length=8,max_length=18,widget=forms.PasswordInput)
    email = forms.EmailField()

    def clean_username(self):
        username = self.cleaned_data['username']

        if not username.isalnum():
            raise ValidationError('Никнейм должен быть без символов')
        
        check_username = User.objects.filter(username=username).exists()

        if check_username is True:
            raise ValidationError('Никнейм уже был занят другим пользователям ')

        return username
    
    def clean_password(self):
        password = self.cleaned_data['password']

        if not any(num.isdigit() for num in password):
            raise ValidationError('Пароль должен иметь хотя бы одну цифру')
        
        if not any(abc.isalpha() for abc in password):
            raise ValidationError('Пароль должен иметь хотя бы одну букву')
        
        return password
    
    def clean(self):
        cleaned_data = super().clean()
        try:
            username = cleaned_data['username']
            password = cleaned_data['password']

            if username == password:
                raise ValidationError('Никнейм не должен быть одинаковым как Пароль')
        
        except KeyError:
            pass
        return cleaned_data