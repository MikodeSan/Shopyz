from django.db import models
from django.contrib.auth.models import User


from .shop import Shop, ShopProduct


class Order(models.Model):
    """Self-explanatory"""

    reference = models.CharField(max_length=120)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    order_date = models.DateTimeField("purchase date")
    # shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    # products = models.ManyToMany(Question, on_delete=models.CASCADE)


class ShopOrder(models.Model):
    """Self-explanatory"""

    reference = models.CharField(max_length=120, blank=False, null=False, default="")
    shop = models.ForeignKey(Shop, blank=True, null=True, on_delete=models.SET_NULL)
    order = models.ForeignKey(Order, blank=True, null=True, on_delete=models.CASCADE)


class Item(models.Model):
    """Self-explanatory"""

    shop_order = models.ForeignKey(
        ShopOrder, blank=False, null=True, on_delete=models.CASCADE
    )
    product_reference = models.ForeignKey(
        ShopProduct, blank=True, null=True, on_delete=models.SET_NULL
    )
    unit_price = models.FloatField(default=0)
    devise = models.CharField(max_length=120, blank=True, null=True, default="")
    quantity = models.FloatField(default=0)
    unit = models.CharField(max_length=42, blank=True, null=True, default="")
