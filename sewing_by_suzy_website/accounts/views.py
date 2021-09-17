from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Customer, Employee
from .serializers import AccountSerializer
from django.contrib.auth.models import User


# Create your views here.
