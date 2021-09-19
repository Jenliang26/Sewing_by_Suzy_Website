from django.http.response import Http404
from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Orders, Statuses, Garment
from .serializers import OrderSerializer
from django.contrib.auth.models import User
from django.http import Http404

# Create your views here.
class OrderList (APIView):

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
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.update(order, request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        order = self.get_inventory(pk)
        serializer = OrderSerializer(order)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)