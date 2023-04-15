from django.db import models

from .product import Product


class Shop(models.Model):
    """Self-explanatory"""

    label = models.CharField(max_length=120, blank=False, null=False, default="")
    url = models.URLField(blank=True, null=True, default="")


class ProductReference(models.Model):
    """Self-explanatory"""

    reference = models.CharField(max_length=120, blank=False, null=False, default="")
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    availablity = models.BooleanField(default=True)
