from django.db import models
from django.contrib.auth import models as auth_models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Shop(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    shops = models.ManyToManyField(Shop, related_name='categories')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProductInfo(models.Model):
    product = models.ForeignKey(Product, related_name='info', on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, related_name='product_infos', on_delete=models.CASCADE)
    name = models.ForeignKey(Product, related_name='product' , on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_rrc = models.DecimalField(max_digits=10, decimal_places=2)   

    def __str__(self):
        return f"{self.name} - {self.shop}" 


class Parameter(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProductParameter(models.Model):
    product_info = models.ForeignKey(ProductInfo, related_name='parameters', on_delete=models.CASCADE)
    parameter = models.ForeignKey(Parameter, related_name='product_parameters', on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.parameter.name}: {self.value}"
    

class Order(models.Model):
    dt = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, related_name='order_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()


class Contact(models.Model):

    type = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)