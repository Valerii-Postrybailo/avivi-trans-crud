from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


from .views import main_page, forbidden, health_check

from apps.crud_transaction.urls import router as crud_transaction_router
from apps.user import urls as user_urls
from apps.tg_bot import urls as tg_bots_urls
from apps.store import urls as store_urls


urlpatterns = [
    path('', main_page, name='main_page'),

    path('admin/', admin.site.urls),

    path('', include(crud_transaction_router.urls)),
    path('', include(user_urls)),
    path('', include(tg_bots_urls)),
    path('', include(store_urls)),

    path('forbidden/', forbidden, name='forbidden'),
    path('health/', health_check, name='health_check'),

    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)