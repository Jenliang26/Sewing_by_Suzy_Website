from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Reviews(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField(null=True)
    number_rating = models.IntegerField(default= 4, validators=[MaxValueValidator(5), MinValueValidator(1)])
    comment = models.CharField(max_length=500)