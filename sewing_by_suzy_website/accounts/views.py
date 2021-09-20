from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Customer, Employee
from .serializers import EmployeeSerializer, CustomerSerializer
from django.contrib.auth.models import User
from django.http import Http404



# Create your views here.
class Customers(APIView):

    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_customer(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        customer = self.get_customer(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

class Customer_By_User(APIView):

    def get_customer(self, uid):
        try:
            return Customer.objects.get(user_id=uid)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, uid):
        customer = self.get_customer(uid)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, uid):
        customer = self.get_customer(uid)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.update(customer, request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Employees(APIView):

    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_employee(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        employee = self.get_employee(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

class Employee_By_User(APIView):

    def get_employee(self, uid):
        try:
            return Employee.objects.get(user_id=uid)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, uid):
        employee = self.get_employee(uid)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, uid):
        employee = self.get_employee(uid)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.update(employee, request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        



class CustomerList(APIView):

    permissioin_classes = [AllowAny]

    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

class EmployeeList(APIView):

    permissioin_classes = [AllowAny]

    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

class DisplayCustomer(APIView):

    def get_customer(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        customer = self.get_customer(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, pk):
        customer = self.get_customer(pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.update(customer, request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



