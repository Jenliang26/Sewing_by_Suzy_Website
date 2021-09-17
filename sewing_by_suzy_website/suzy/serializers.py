from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import User, Customer, Orders, Statuses, Garment, Inventory, Reviews

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'user', 'name', 'phone_number', 'email']

class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['id', 'customer', 'date', 'notes', 'status']

class StatusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statuses
        fields = ['id', 'status']

class GarmentSerializer(serializers.ModelSerializer):
    class Meta:
        models = Garment
        fields = ['id', 'order', 'type', 'quantity']

class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        models = Reviews
        fields = ['id', 'name', 'date', 'number_rating', 'comment']
