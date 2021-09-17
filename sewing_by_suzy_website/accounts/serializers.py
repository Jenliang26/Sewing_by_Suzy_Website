from rest_framework import serializers
from .models import Customer, Employee

class CustomerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Customer
        fields = ['user', 'id', 'name', 'role'] 

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Employee
        fields = ['user', 'id', 'name', 'role'] 
        