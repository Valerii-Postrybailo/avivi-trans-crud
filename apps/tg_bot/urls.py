from django.urls import path
from . import views

urlpatterns = [
    path('bots/', views.TelegramSettingsView.as_view(), name='tg_bot_list'),
    path('bots/<int:pk>/', views.TelegramSettingsView.as_view(), name="tg_bot_operation_by_id"),

    path('bot_webhook/<int:bot_id>/', views.bot_service, name="webhook"),
    path('change_webhook_state/', views.change_webhook_state_view, name="set_webhook"),
]