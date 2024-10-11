from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.TelegramUserView.as_view(), name='tg_users_list'),
    path('users/<int:pk>/', views.TelegramUserView.as_view(), name='tg_users_operations_by_id')
]