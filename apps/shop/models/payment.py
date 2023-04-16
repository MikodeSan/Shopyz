from django.db import models

from .order import Order


class Payment(models.Model):
    """Self-explanatory"""

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
