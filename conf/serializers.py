from rest_framework import serializers
from .models import Category, Customer, Product, ShopCart, Item

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'location', 'email', 'number', 'date']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'price', 'start_date', 'end_date']

class ShopCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopCart
        fields = ['id', 'date', 'owner', 'total_price', 'payment']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'product', 'sell_date', 'cart']
