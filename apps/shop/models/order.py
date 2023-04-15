from django.db import models

from .shop import Shop
from .product import Product


class Order(models.Model):
    """Self-explanatory"""

    reference = models.CharField(max_length=120)
    # user = models.ForeignKey(User, on_delete=models.SET_NULL)
    order_date = models.DateTimeField("purchase date")
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    # products = models.ManyToMany(Question, on_delete=models.CASCADE)


class Item(models.Model):
    """Self-explanatory"""

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit_price = models.FloatField(default=0)
    devise = models.CharField(max_length=120)
    quantity = models.IntegerField(default=0)
