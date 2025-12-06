from django.contrib import admin
import random
from .models import Products,Cart_Item,Cart,Profile_Context,Category
# Register your models here.

admin.site.register(Products)
admin.site.register(Cart_Item)
admin.site.register(Cart)
admin.site.register(Profile_Context)
admin.site.register(Category)

admin_time = 1000

keys_randint_timeout = {
        'profile' : random.randint(1,admin_time)
    }