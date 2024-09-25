import requests

from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters

from .handlers import *
from apps.tg_bot.models import TelegramSettings

bot_instance = None
dispatcher_instance = None


def initialize_bot():
    global bot_instance, dispatcher_instance
    if not bot_instance or not dispatcher_instance:
        bot_instance = Bot(token="your harcode token")
        dispatcher_instance = Dispatcher(bot_instance, None, use_context=True)

        dispatcher_instance.add_handler(CommandHandler('start', start))
        dispatcher_instance.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_language_selection))


def get_bot_settings(bot_token):
    try:
        settings = TelegramSettings.objects.get(api_key=bot_token)
        print("settings", settings)
        return settings
    except TelegramSettings.DoesNotExist:
        raise ValueError(f"Bot settings with token {bot_token} does not exist.")


def set_remove_webhook(settings):
    webhook_info_url = f"https://api.telegram.org/bot{settings.api_key}/getWebhookInfo"
    set_webhook_url = f"https://api.telegram.org/bot{settings.api_key}/setWebhook"
    delete_webhook_url = f"https://api.telegram.org/bot{settings.api_key}/deleteWebhook"

    webhook_info_response = requests.get(webhook_info_url)

    if webhook_info_response.json()['result']['url']:
        requests.post(delete_webhook_url)
        print("Webhook deleted!")
    else:
        requests.post(set_webhook_url, data={'url': "https://valeratest.serveo.net/bot_webhook/"})
        print("Webhook is working!")
