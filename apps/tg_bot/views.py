import json

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy, reverse
from django.http import JsonResponse

from .models import TelegramSettings
from .forms import TelegramSettingsCreateForm
from .mixins import SuperUserRequiredMixin
from .bot import bot


class TelegramSettingsView(SuperUserRequiredMixin, View):

    template_settings_list = 'bot_management.html'

    def get(self, request):
        tg_settings_list = TelegramSettings.objects.all()
        return render(request, self.template_settings_list, {'tg_bots': tg_settings_list})

    def post(self, request):
        form = TelegramSettingsCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('tg_bot_list'))
        return render(request, self.template_settings_list, {'form': form})

    def patch(self, request, *args, **kwargs):
        bot_id = kwargs.get('pk')
        telegram_bot = get_object_or_404(TelegramSettings, id=bot_id)

        data = json.loads(request.body)

        updatable_fields = ['bot_name', 'api_key', 'webhook_url']
        fields_to_update = []

        for field in updatable_fields:
            if field in data and getattr(telegram_bot, field) != data[field]:
                setattr(telegram_bot, field, data[field])
                fields_to_update.append(field)

        if fields_to_update:
            telegram_bot.save(update_fields=fields_to_update)
            return JsonResponse({}, status=200)
        else:
            return JsonResponse({}, status=400)

    def delete(self, request, *args, **kwargs):
        bot_id = kwargs.get('pk')
        telegram_bot = get_object_or_404(TelegramSettings, id=bot_id)
        telegram_bot.delete()

        return JsonResponse({}, status=204)


@csrf_exempt
def bot_service(request):
    print("bot working!")
    return JsonResponse({"status": "ok"}, status=200)


@csrf_exempt
def set_remove_webhook(request):
    if request.method == "POST":
        bot_id = request.POST.get('bot_id')
        try:
            bot.set_remove_webhook(bot_id)
        except:
            print("Smth went wrong...")

        return redirect(reverse('tg_bot_list'))
