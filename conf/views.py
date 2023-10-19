from django.shortcuts import render
from rest_framework import generics
from .models import Customer, ShopCart,Product,Category,
from .serializers import ShopCartSerializer,CategorySerializer,ProductSerializer,CustomerSerializer
from rest_framework.response import Response
from django.db.models import Sum

class TotalProductView(generics.ListAPIView):
 
    def get(self, request, *args, **kwargs):
        total = Product.objects.all().aggregate(Sum('price'))['price__sum']
        return Response({"total_price": total})

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CustomerListCreate(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ShoppingCartListCreate(generics.ListCreateAPIView):
    queryset = ShopCart.objects.all()
    serializer_class = ShopCartSerializer


class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CustomerRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class ShoppingCartRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShopCart.objects.all()
    serializer_class = ShopCartSerializer

class CustomerPurchaseHistoryView(generics.ListAPIView):
    serializer_class = ShopCartSerializer

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        return ShopCart.objects.filter(owner__id=customer_id)