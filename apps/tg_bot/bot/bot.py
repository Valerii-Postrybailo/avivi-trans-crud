import requests

from telegram import Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters

from .handlers import *
from apps.tg_bot.models import TelegramSettings

bot_instance = None
dispatcher_instance = None


def initialize_bot(settings):
    global bot_instance, dispatcher_instance
    if not bot_instance or not dispatcher_instance:
        bot_instance = Bot(token=settings.api_key)
        dispatcher_instance = Dispatcher(bot_instance, None, use_context=True)

        dispatcher_instance.add_handler(CommandHandler('start', start))
        dispatcher_instance.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_language_selection))


def get_bot_settings(bot_id):
    try:
        settings = TelegramSettings.objects.get(id=bot_id)
        return settings
    except TelegramSettings.DoesNotExist:
        raise ValueError(f"Bot settings with ID {bot_id} does not exist.")


def set_remove_webhook(settings, bot_id):
    webhook_info_url = f"https://api.telegram.org/bot{settings.api_key}/getWebhookInfo"
    set_webhook_url = f"https://api.telegram.org/bot{settings.api_key}/setWebhook"
    delete_webhook_url = f"https://api.telegram.org/bot{settings.api_key}/deleteWebhook"

    webhook_info_response = requests.get(webhook_info_url)

    if webhook_info_response.json()['result']['url']:
        requests.post(delete_webhook_url)
        print("Webhook deleted!")
    else:
        requests.post(set_webhook_url, data={'url': f"{settings.webhook_url}/bot_webhook/{bot_id}/"})
        print("Webhook is working!")
