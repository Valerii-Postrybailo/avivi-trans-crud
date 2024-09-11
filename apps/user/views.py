from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .models import TelegramUser
from .forms import TelegramUserForm


class TelegramUserList(generic.ListView):
    model = TelegramUser
    template_name = 'tg_users.html'
    context_object_name = 'tg_users_list'


class TelegramUserCreate(generic.CreateView):
    model = TelegramUser
    template_name = 'add_tg_users.html'
    form_class = TelegramUserForm
    success_url = reverse_lazy('tg_users_list')


class TelegramUserDelete(generic.DeleteView):
    model = TelegramUser
    template_name = 'tg_users.html'
    success_url = reverse_lazy('tg_users_list')
