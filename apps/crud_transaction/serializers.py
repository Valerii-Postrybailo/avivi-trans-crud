from rest_framework import serializers
from .models import User, Balance, Transaction


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "telegram_id"]


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = ['id', 'user', 'amount']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'user', 'hash', 'amount', 'date']

    def create(self, validated_data):
        user = validated_data['user']
        amount = validated_data['amount']
        transaction_hash = validated_data['hash']

        if Transaction.objects.filter(hash=transaction_hash).exists():
            raise serializers.ValidationError("Transaction with this hash already exists.")

        try:
            balance = Balance.objects.get(user=user)
        except Balance.DoesNotExist:
            raise serializers.ValidationError("User balance does not exist!")

        transaction = Transaction.objects.create(**validated_data)

        balance.amount += amount
        balance.save()

        return transaction
