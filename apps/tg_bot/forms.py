from django import forms

from .models import TelegramSettings


class TelegramSettingsCreateForm(forms.ModelForm):
    class Meta:
        model = TelegramSettings
        fields = ['bot_name', 'api_key', 'webhook_url']