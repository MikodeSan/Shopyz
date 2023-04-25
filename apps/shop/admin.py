from django.contrib import admin

from .models import Order, ShopOrder, Item, Payment, Shop, ShopProduct, Product

admin.site.register(Order)
admin.site.register(ShopOrder)
admin.site.register(Item)
admin.site.register(Payment)
admin.site.register(Shop)
admin.site.register(ShopProduct)
admin.site.register(Product)
