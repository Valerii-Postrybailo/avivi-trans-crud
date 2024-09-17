from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from .views import main_page
from apps.user import urls as user_urls

from apps.crud_transaction.views import (
    UsersViewSet,
    BalancesViewSet,
    TransactionsViewSet
)

router = routers.SimpleRouter()

router.register(r'user', UsersViewSet)
router.register(r'balance', BalancesViewSet)
router.register(r'transaction', TransactionsViewSet)

urlpatterns = [
    path('', main_page, name='main_page'),
    path('admin/', admin.site.urls),

    path('', include(router.urls)),
    path('', include(user_urls)),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
