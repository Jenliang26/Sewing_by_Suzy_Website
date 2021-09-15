from django.contrib import admin
from .models import User, Customer, Orders, Statuses, Garment, Inventory, Reviews


# Register your models here.
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Orders)
admin.site.register(Statuses)
admin.site.register(Garment)
admin.site.register(Inventory)
admin.site.register(Reviews)

