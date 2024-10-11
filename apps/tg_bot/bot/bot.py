import requests

from django.conf import settings

from telegram import Bot
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

from .handlers import start, handle_menu_selection, product_detail, handle_callback_query, show_catalog
from apps.tg_bot.models import TelegramSettings

TELEGRAM_API_URL = settings.TELEGRAM_API_URL

bot_instance = None
dispatcher_instance = None


def initialize_bot(settings):
    global bot_instance, dispatcher_instance
    if not bot_instance or not dispatcher_instance:
        bot_instance = Bot(token=settings.api_key)
        dispatcher_instance = Dispatcher(bot_instance, None, use_context=True)

        dispatcher_instance.add_handler(CommandHandler(['start', 'restart'], start))
        dispatcher_instance.add_handler(CommandHandler("catalog", show_catalog))

        dispatcher_instance.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_menu_selection))

        dispatcher_instance.add_handler(
            CallbackQueryHandler(lambda update, context: product_detail(update, context, settings),
                                 pattern=r'^product_'))

        dispatcher_instance.add_handler(CallbackQueryHandler(handle_callback_query))


def get_bot_settings(bot_id):
    try:
        settings = TelegramSettings.objects.get(id=bot_id)
        return settings
    except TelegramSettings.DoesNotExist:
        raise ValueError(f"Bot settings with ID {bot_id} does not exist.")


def change_webhook_state(settings, bot_id):
    webhook_info_url = f"{TELEGRAM_API_URL}/bot{settings.api_key}/getWebhookInfo"
    set_webhook_url = f"{TELEGRAM_API_URL}/bot{settings.api_key}/setWebhook"
    delete_webhook_url = f"{TELEGRAM_API_URL}/bot{settings.api_key}/deleteWebhook"

    webhook_info_response = requests.get(webhook_info_url)

    if webhook_info_response.json()['result']['url']:
        requests.post(delete_webhook_url)
        print("Webhook deleted!")
    else:
        requests.post(set_webhook_url, data={'url': f"{settings.webhook_url}/bot_webhook/{bot_id}/"})
        print("Webhook is working!")
