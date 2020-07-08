from __future__ import unicode_literals
from django.db import models
from login_app.models import User
from decimal import Decimal

class Category(models.Model):
    name = models.CharField(max_length=255)
    parent_category = models.ForeignKey('self', null = True, blank = True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(blank=True)
    stock = models.PositiveIntegerField(default=100)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    amount_sold = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def discount(self, discount):
        self.price = Decimal(float(self.price)-(float(self.price)*(discount / 100)))
        self.save()
    
    def markup(self,percent):
        self.price= Decimal(float(self.price)+(float(self.price)*(percent / 100)))
        self.save()

class Cart(models.Model):
    user = models.ForeignKey(User, related_name="has_cart", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def itemTotal(self):
        return self.has_products.all().count()

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    cart = models.ForeignKey(Cart, related_name="has_products", on_delete=models.CASCADE)

    def totalPrice(self):
        return self.product.price * self.quantity

    




