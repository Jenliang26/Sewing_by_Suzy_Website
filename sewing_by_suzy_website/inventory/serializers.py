from rest_framework import serializers
from .models import Inventory

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        models = Inventory
        fields = ['id', 'name', 'description', 'quantity', 'category']