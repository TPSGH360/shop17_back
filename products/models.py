from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    TYPE_CHOICES = [
        ("phone", "Phone"),
        ("accessory", "Accessory"),
        ("laptop", "Laptop"),
    ]

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="products/", null=True, blank=True)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, default="phone")
    manufacturer = models.CharField(max_length=255, null=True, blank=True)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cart")
    items = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.user.username}'s Cart"
