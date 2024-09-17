from django.urls import path
from . import views

urlpatterns = [
    path('bots/', views.TelegramSettingsList.as_view(), name='tg_bot_list'),
    path('bots_create/', views.TelegramSettingsCreate.as_view(), name="tg_bot_creating"),
    path('bots_delete/<int:pk>/', views.TelegramSettingsDelete.as_view(), name="tg_bot_deleting"),
    path('bots_update/<int:pk>/', views.TelegramSettingsUpdate.as_view(), name="tg_bot_updating"),

    path('bot_set_webhook', views.enable_webhook_view, name="set_webhook"),

    path('forbidden/', views.forbidden, name='forbidden'),
]
