from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from crud_transaction.views import (
    UsersViewSet,
    BalancesViewSet,
    TransactionsViewSet
)

router = routers.SimpleRouter()
router.register(r'user', UsersViewSet)
router.register(r'balance', BalancesViewSet)
router.register(r'transaction', TransactionsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
