from django.http.response import Http404
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Orders, Garment
from .serializers import OrderSerializer, GarmentSerializer
from django.contrib.auth.models import User
from django.http import Http404
from twilio.rest import Client 

# Create your views here.
class OrderView(APIView):

    def get(self, request):
        order = Orders.objects.all()
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrderDetail(APIView):

    def get_orders(self, pk):
        try:
            return Orders.objects.get(pk=pk)
        except Orders.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        order = self.get_orders(pk)
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, pk):
        order = self.get_orders(pk)
        # self.sendsms(order, request.data)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.update(order, request.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        order = self.get_orders(pk)
        serializer = OrderSerializer(order)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def sendsms(self, order, neworder):
        account_sid = 'AC2fb817a44166d0638f4ab6295b624808'
        auth_token = '6aab9028271cd65c255fb028b3b98b9f'
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body = "Your new order status has been changed from Sewing By Suzy.",
            from_ = "+13344234248",
            to = "+14147920957"
        )

class GarmentList(APIView):

    def post(self,request):
        serializer = GarmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get_garments(self, orderpk):
        try:
            return Garment.objects.filter(order=orderpk)
        except Garment.DoesNotExist:
            raise Http404

    def get(self, request, orderpk):
        garment = self.get_garments(orderpk)
        serializer = GarmentSerializer(garment, many=True)
        return Response(serializer.data)

class CustomerOrders(APIView):

    def get_orders(self, customerid):
        try:
            return Orders.objects.filter(customer=customerid)
        except Orders.DoesNotExist:
            raise Http404

    def get(self, request, customerid):
        order = self.get_orders(customerid)
        serializer = OrderSerializer(order, many=True)
        return Response(serializer.data)