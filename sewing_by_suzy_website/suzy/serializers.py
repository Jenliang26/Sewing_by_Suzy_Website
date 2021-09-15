from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import User, Customer, Orders, Statuses, Garment, Inventory, Reviews

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'role']

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['user', 'name', 'phone_number', 'email']

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['customer', 'date', 'notes', 'status']

class StatusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statuses
        fields = ['status']

class GarmentSerializer(serializers.ModelSerializer):
    class Meta:
        models = Garment
        fields = ['order', 'type', 'quantity']

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        models = Inventory
        fields = ['name', 'description', 'quantity', 'category']

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        models = Reviews
        fields = ['name', 'date', 'number_rating', 'comment']