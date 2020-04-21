from django.db import models
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import UserSerializer,CreateUserSerializer,LoginUserSerializer
from rest_framework.authtoken.models import Token
# Create your models here.

    
class Access(generics.ListCreateAPIView,APIView):
    def post(self,request):
        print(request.data["username"])
        username = request.data["username"]
        password = request.data["password"]
        user = authenticate(request, username=username, password=password)
        print(password)
        if user is not None:
            print(user)

            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'username': user.username,
                'email': user.email
            })         
        else:
            return Response({
                    'msg':"user not registered",
                })         
    # No backend authenticated the credentials
        
        

class Auth(generics.ListCreateAPIView,APIView):
    def post(self,request):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        user = User.objects.create_user(username=username,email=email,password=password)
        user.save()
        
        return Response({"msg":"User created"})    
