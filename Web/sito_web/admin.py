from django.contrib import admin
from .models import Products,Cart_Item,Cart
# Register your models here.

admin.site.register(Products)
admin.site.register(Cart_Item)
admin.site.register(Cart)