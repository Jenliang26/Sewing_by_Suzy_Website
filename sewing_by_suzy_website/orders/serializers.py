from rest_framework import serializers
from .models import Orders, Garment

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        models = Orders
        fields = ['id', 'customer', 'date', 'notes', 'status']

class GarmentSerializer(serializers.ModelSerializer):
    class Meta:
        models = Garment
        fields = ['id', 'order', 'type', 'quantity']