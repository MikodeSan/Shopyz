from django.db import models


class Product(models.Model):
    """Self-explanatory"""

    label = models.CharField(max_length=120, blank=False, null=False, default="")
    size = models.URLField(blank=True, null=True, default="")
    length = models.FloatField(blank=True, null=True, default=0)
    height = models.FloatField(blank=True, null=True, default=0)
    depth = models.FloatField(blank=True, null=True, default=0)
    dimension_unit = models.CharField(
        max_length=120, blank=False, null=False, default=""
    )
    weight = models.FloatField(blank=True, null=True, default=0)
    weight_unit = models.CharField(max_length=120, blank=False, null=False, default="")
