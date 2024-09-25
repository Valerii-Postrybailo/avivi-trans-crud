from rest_framework import routers

from .views import (
    UsersViewSet,
    BalancesViewSet,
    TransactionsViewSet
)

router = routers.SimpleRouter()

router.register(r'user', UsersViewSet)
router.register(r'balance', BalancesViewSet)
router.register(r'transaction', TransactionsViewSet)