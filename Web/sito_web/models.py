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

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}"

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2 )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    imagin = models.ImageField(upload_to='products/', 
                                blank=True,
                                validators=[FileExtensionValidator(['jpg','webp','png'])])

    class Meta:
        indexes = [
            models.Index(fields=['price']),
            models.Index(fields=['name']),
            models.Index(fields=['category'])
        ]

    def __str__(self):
        return f'name:{self.name} price:{self.price} category {self.category}'
 
class Cart_Item(models.Model):
    cart = models.ForeignKey(Cart , on_delete=models.CASCADE)
    product= models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        indexes = [
            models.Index(fields=['cart'])
        ]

    def __str__(self):
        return f'cart:{self.cart} product:{self.product} quatity:{self.quantity}'
#class Cart(models.Model):
#    user = models.OneToOneField(User , on_delete=models.CASCADE)
#    product_name = models.CharField(max_length=100)
#    price = models.DecimalField(max_digits=10, decimal_places=2 )
#    imagin = models.ImageField()

class Profile_Context(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    context = models.CharField(max_length=100,default='')
    ava = models.ImageField(upload_to='avatar/')
    def __str__(self):
        return f'first_name:{self.user.first_name},last_name:{self.user.last_name},context:{self.context}'
    