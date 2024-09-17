from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.TelegramUserList.as_view(), name='tg_users_list'),
    path('users_create/', views.TelegramUserCreate.as_view(), name='create_users'),
    path('users_deleted/<int:pk>/', views.TelegramUserDelete.as_view(), name='tg_users_deleting'),
]