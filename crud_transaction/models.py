import uuid

from django.db import models
from django.utils import timezone


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=50, unique=True)
    telegram_id = models.PositiveBigIntegerField(unique=True)


class Balance(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


class Transaction(models.Model):
    id: models.AutoField(primary_key=True)
    user: models.ForeignKey('User', on_delete=models.CASCADE)
    hash: models.CharField(max_length=64, unique=True)
    amount: models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    date: models.DateTimeField(default=timezone.now)
