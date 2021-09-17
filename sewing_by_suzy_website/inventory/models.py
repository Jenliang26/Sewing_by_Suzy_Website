from django.db import models

# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    quantity = models.IntegerField(null = True)
    category = models.CharField(max_length=50)