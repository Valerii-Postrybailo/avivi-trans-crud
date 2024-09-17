from django.db import models


class TelegramSettings(models.Model):
    bot_name = models.CharField(max_length=50)
    api_key = models.CharField(max_length=250)
    webhook_url = models.URLField()
    host = models.CharField(max_length=255, default="localhost")
    port = models.PositiveIntegerField(default=8443)
