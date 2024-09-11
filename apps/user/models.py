from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    profile_description = models.CharField(max_length=50)


class TelegramUser(models.Model):

    LANG_CHOICES = [
        ("en", "English"),
        ("uk", "Ukrainian")
    ]

    telegram_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25, unique=True)
    first_name = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=50, unique=True)
    lang = models.CharField(max_length=10, choices=LANG_CHOICES, default='en')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
