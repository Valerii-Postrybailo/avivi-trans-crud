from django.shortcuts import render
from django.utils import timezone
from django.db.models import Sum

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse, OpenApiExample

from .models import User, Balance, Transaction
from .serializers import UserSerializer, BalanceSerializer, TransactionSerializer


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BalancesViewSet(viewsets.ModelViewSet):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer


class TransactionsViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    @extend_schema(
        operation_id='get_transactions_by_period',
        parameters=[
            OpenApiParameter('days', type=int, description='Number of days to filter transactions', required=False)
        ],
        responses={
            200: OpenApiResponse(
                response=TransactionSerializer(many=True),  # Якщо є серіалізатор
                description='A list of transactions and total amount within the period',
                examples=[
                    OpenApiExample(
                        name="Example Response",
                        value={
                            'transaction_count': 123,
                            'total_amount': 456.78
                        },
                        response_only=True,
                        media_type='application/json'  # Вказати медіа тип
                    )
                ]
            )
        }
    )
    @action(methods=['get'], detail=False)
    def trans_and_amount_by_period(self, request):
        days = int(request.query_params.get('days', 3))
        end_date = timezone.now()
        start_date = end_date - timezone.timedelta(days=days)
        transactions = Transaction.objects.filter(date__range=(start_date, end_date))
        transaction_count = transactions.count()
        total_amount = transactions.aggregate(Sum('amount'))['amount__sum'] or 0

        return Response({
            'transaction_count': transaction_count,
            'total_amount': total_amount,
        })
