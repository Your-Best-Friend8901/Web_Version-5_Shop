from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.
class Code_save(models.Model):
    user_id = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    def __str__(self):
        return f'id:{self.user_id} code:{self.code}'
    

class Cart(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2 )
    category = models.CharField(max_length=50) 
    imagin = models.ImageField(upload_to='products/', 
                                blank=True,
                                validators=[FileExtensionValidator(['jpg','webp','png'])])

    def __str__(self):
        return f'name:{self.name} price:{self.price} category {self.category}'
 
class Cart_Item(models.Model):
    cart = models.ForeignKey(Cart , on_delete=models.CASCADE)
    product= models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'cart:{self.cart} product:{self.product} quatity:{self.quantity}'
#class Cart(models.Model):
#    user = models.OneToOneField(User , on_delete=models.CASCADE)
#    product_name = models.CharField(max_length=100)
#    price = models.DecimalField(max_digits=10, decimal_places=2 )
#    imagin = models.ImageField()
    