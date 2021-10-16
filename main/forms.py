from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(label='Email',  widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class CreateSurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['survey_name', 'end_date', 'survey_description']
        widgets = {
            'survey_name': forms.TextInput(attrs={'class': 'form-control', 'name':'survey_name'}),
            'survey_description': forms.TextInput(attrs={'class': 'form-control', 'name':'survey_description'}),
            'end_date': forms.DateTimeInput(attrs={'class': 'form-control', 'name':'end_date', 'type':'date'}),
        }

class UpdateSurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['survey_name', 'end_date', 'survey_description']
        widgets = {
            'survey_name': forms.TextInput(attrs={'class': 'form-control', 'name':'survey_name'}),
            'survey_description': forms.TextInput(attrs={'class': 'form-control', 'name':'survey_description'}),
            'end_date': forms.DateTimeInput(attrs={'class': 'form-control', 'name':'end_date', 'type':'date'}),
        }