from django.db import models
from django.utils import timezone
class Category(models.Model):
    name = models.CharField(max_length=255)

class Customer(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    number = models.CharField(max_length=20) # Phone number
    date = models.DateTimeField( default=timezone.now)

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=7, decimal_places=2) # Assume price factor including cents
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True, blank=True)

class ShopCart(models.Model):
    date = models.DateTimeField(auto_now_add=True, default=timezone.now)
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='carts')
    total_price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
    payment = models.CharField(max_length=200, null=True, blank=True)

class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    sell_date = models.DateTimeField( null=True, blank=True)
    cart = models.ForeignKey(ShopCart, on_delete=models.CASCADE, related_name='items')
