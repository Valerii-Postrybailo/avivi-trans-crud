from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.StoreItemsView.as_view(), name='products_list_page'),
    path('products/add/', views.ProductCreateView.as_view(), name='create_product_page'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='delete_product'),
    path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name='update_product'),
]