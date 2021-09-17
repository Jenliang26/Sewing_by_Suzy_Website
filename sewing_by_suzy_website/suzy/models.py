from django.db import models
from django.db.models.expressions import Value
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Orders(models.Model):
    customer = models.ForeignKey('Customer', blank=True, null=True, on_delete=models.PROTECT)
    date = models.DateField(null=True)
    notes = models.CharField(max_length=500)
    status = models.ForeignKey('Statuses', blank=True, null=True, on_delete=models.PROTECT)

class Statuses(models.Model):
    status = models.CharField(max_length=80)

class Garment(models.Model):
    order = models.ForeignKey('Orders', blank=True, null=True, on_delete=models.PROTECT)
    type = models.CharField(max_length=50)
    quantity = models.IntegerField(null = True)

class Inventory(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    quantity = models.IntegerField(null = True)
    category = models.CharField(max_length=50)

class Reviews(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField(null=True)
    number_rating = models.IntegerField(default= 4, validators=[MaxValueValidator(5), MinValueValidator(1)])
    comment = models.CharField(max_length=500)

