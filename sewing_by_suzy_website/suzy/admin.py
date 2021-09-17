from django.contrib import admin
from .models import Customer, Orders, Statuses, Garment, Inventory, Reviews
from django.contrib.auth.models import User


# Register your models here.
admin.site.register(Customer)
admin.site.register(Orders)
admin.site.register(Statuses)
admin.site.register(Garment)
admin.site.register(Inventory)
admin.site.register(Reviews)

