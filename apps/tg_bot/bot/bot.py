import requests

from apps.tg_bot.models import TelegramSettings


def set_remove_webhook(bot_id):
    try:
        settings = TelegramSettings.objects.get(id=bot_id)
    except TelegramSettings.DoesNotExist:
        raise ValueError(f"Bot settings with ID {bot_id} does not exist.")

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
