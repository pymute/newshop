from django.urls import path
from .views import CustomerPurchaseHistoryView,TotalProductView
from .views import (
    CategoryListCreate, ProductListCreate, CustomerListCreate, ShoppingCartListCreate,
    CategoryRetrieveUpdateDestroy, ProductRetrieveUpdateDestroy, CustomerRetrieveUpdateDestroy, ShoppingCartRetrieveUpdateDestroy
)

urlpatterns = [
    path('customer/<int:customer_id>/purchases/', CustomerPurchaseHistoryView.as_view(), name='customer-purchases'),
    path('total-product-value/', TotalProductView.as_view(), name='total-product-value'),
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroy.as_view(), name='category-detail'),
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroy.as_view(), name='product-detail'),
    path('customers/', CustomerListCreate.as_view(), name='customer-list-create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroy.as_view(), name='customer-detail'),
    path('shopping-cart/', ShoppingCartListCreate.as_view(), name='shopping-cart-list-create'),
    path('shopping-cart/<int:pk>/', ShoppingCartRetrieveUpdateDestroy.as_view(), name='shopping-cart-detail'),
]
