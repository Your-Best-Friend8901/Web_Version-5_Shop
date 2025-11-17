from django.contrib import admin
from .models import Products,Cart_Item,Cart,Profile_Context,Category
# Register your models here.

admin.site.register(Products)
admin.site.register(Cart_Item)
admin.site.register(Cart)
admin.site.register(Profile_Context)
admin.site.register(Category)