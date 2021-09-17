from django.contrib import admin
from .models import Orders, Statuses, Garment

# Register your models here.
admin.site.register(Orders)
admin.site.register(Statuses)
admin.site.register(Garment)


