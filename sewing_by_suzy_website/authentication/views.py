from django.contrib.auth.models import User
from rest_framework.views import APIView
from .serializers import UserSerializer, RegisterSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.http import Http404
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token



# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class UserProfile(APIView):
    def get_user(self, uid):
        try:
            return User.objects.filter(pk=uid)[0]
        except User.DoesNotExist:
            raise Http404
    
    def get(self, request, uid):
        user = self.get_user(uid)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, uid):
        user = self.get_user(uid)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.update(user, request.data)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AllProfiles(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)