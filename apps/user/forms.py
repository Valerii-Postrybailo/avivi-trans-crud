from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, TelegramUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'email')


class TelegramUserForm(forms.ModelForm):
    class Meta:
        model = TelegramUser
        fields = ['username', 'first_name', 'last_name', 'lang']
