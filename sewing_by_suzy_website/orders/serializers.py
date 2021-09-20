from rest_framework import serializers
from .models import Orders, Garment


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['customer', 'date', 'notes', 'status']

class GarmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garment
        fields = ['order', 'type', 'quantity']
        