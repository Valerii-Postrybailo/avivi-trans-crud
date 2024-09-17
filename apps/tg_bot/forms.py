from django import forms

from .models import TelegramSettings


class TelegramSettingsCreateForm(forms.ModelForm):
    class Meta:
        model = TelegramSettings
        fields = ['bot_name', 'api_key', 'webhook_url']


class TelegramSettingsUpdateForm(forms.ModelForm):
    class Meta:
        model = TelegramSettings
        fields = ['bot_name', 'api_key', 'host', 'port', 'webhook_url']