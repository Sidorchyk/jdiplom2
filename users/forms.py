from django import forms
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)

from .models import User

# class CustomUserCreationForm(UserCreationForm):
#     password = forms.CharField(widget=forms.HiddenInput())
#     class Meta:
#         model = User
#         fields = '__all__'
#
# class UserLoginForm(AuthenticationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
#
#     class Meta:
#         model = User
#         fields = ('username', 'password')
#
#
# class UserRegistrationForm(UserCreationForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control py-4', 'placeholder': 'Введите имя пользователя'}))
#     phone = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control py-4', 'placeholder': 'Введите номер телефона'}))
#     telegram_id = forms.CharField(widget=forms.TextInput(attrs={
#         'class': 'form-control py-4', 'placeholder': 'Введите id Telegram'}))
#     email = forms.CharField(widget=forms.EmailInput(attrs={
#         'class': 'form-control py-4', 'placeholder': 'Введите адрес эл. почты'}))
#     password1 = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'form-control py-4', 'placeholder': 'Введите пароль'}))
#     password2 = forms.CharField(widget=forms.PasswordInput(attrs={
#         'class': 'form-control py-4', 'placeholder': 'Подтвердите пароль'}))
#
#     class Meta:
#         model = User
#         fields = ('username', 'phone', 'telegram_id', 'email', 'password1', 'password2')
#
#     def save(self, commit=True):
#         user = super(UserRegistrationForm, self).save(commit=True)
#         return user