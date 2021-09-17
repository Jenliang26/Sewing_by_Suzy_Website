from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    user = models.ForeignKey('User', blank=True, null=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=12)

class Employee(models.Model):
    user = models.ForeignKey('User', blank=True, null=True, on_delete=models.PROTECT)
    name = models.CharField(max_length=50)