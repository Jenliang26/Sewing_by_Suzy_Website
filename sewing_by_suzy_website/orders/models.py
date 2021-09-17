from django.db import models
from accounts.models import Customer

# Create your models here.
class Orders(models.Model):
    customer = models.ForeignKey('Customer', blank=True, null=True, on_delete=models.PROTECT)
    date = models.DateField(null=True)
    notes = models.CharField(max_length=500)
    status = models.ForeignKey('Statuses', blank=True, null=True, on_delete=models.PROTECT)