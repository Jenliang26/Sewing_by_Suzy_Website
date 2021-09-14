from django.db import models
from django.db.models.expressions import Value

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)

class Customer(models.Model):
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    phone_number = models.IntegerField(null = True)
    email = models.EmailField(max_length=254)

class Inventory(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    quantity = models.IntegerField(null = True)
    category = models.CharField(max_length=50)