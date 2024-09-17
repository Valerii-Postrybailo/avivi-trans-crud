from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect

from .models import TelegramSettings
from .forms import TelegramSettingsCreateForm, TelegramSettingsUpdateForm
from .bot import bot


class SuperUserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser

    def handle_no_permission(self):
        return redirect('/forbidden/')


def forbidden(request):
    return render(request, 'forbidden.html', status=403)


class TelegramSettingsList(SuperUserRequiredMixin, generic.ListView):
    model = TelegramSettings
    template_name = 'bot_management.html'
    context_object_name = 'tg_bots'


class TelegramSettingsCreate(generic.CreateView):
    model = TelegramSettings
    form_class = TelegramSettingsCreateForm
    success_url = reverse_lazy('tg_bot_list')


class TelegramSettingsDelete(generic.DeleteView):
    model = TelegramSettings
    success_url = reverse_lazy('tg_bot_list')


class TelegramSettingsUpdate(generic.UpdateView):
    model = TelegramSettings
    form_class = TelegramSettingsUpdateForm
    success_url = reverse_lazy('tg_bot_list')


@csrf_protect
def enable_webhook_view(request):
    if request.method == "POST":
        bot_id = request.POST.get('bot_id')
        try:
            bot.set_webhook(bot_id=bot_id)
        except:
            print("Smth went wrong...")

        return redirect(reverse('tg_bot_list'))