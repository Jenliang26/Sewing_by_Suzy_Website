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

class Reviews(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField(null=True)
    number_rating = models.IntegerField('')
    comment = models.CharField(max_length=500)

class Orders(models.Model):
    customer = models.ForeignKey('')???
    date = models.DateField(null=True)
    notes = models.CharField(max_length=500)
    status = ???

class Garment(models.Model):
    order = models.ForeignKey('')???
    type = models.CharField(max_length=50)
    quantity = models.IntegerField(null = True)

