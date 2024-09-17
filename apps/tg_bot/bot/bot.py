from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from apps.tg_bot.models import TelegramSettings


def start(update, context):
    update.message.reply_text('Hello there!')


def echo(update, context):
    update.message.reply_text(update.message.text)


def set_webhook(bot_id):

    try:
        settings = TelegramSettings.objects.get(id=bot_id)
    except TelegramSettings.DoesNotExist:
        raise ValueError(f"Bot settings with ID {bot_id} does not exist.")

    updater = Updater(token=settings.api_key, use_context=True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    webhook_info = updater.bot.get_webhook_info()

    if webhook_info.url:
        updater.bot.delete_webhook()
        print("Webhook deleted!")
    else:
        updater.start_webhook(
            listen=settings.host,
            port=settings.port,
            webhook_url=settings.webhook_url,
        )
        print("Webhook is working!")