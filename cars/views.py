from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken

from .models import Car
from .serializers import CarsSerializer, DeleteCarsSerializer

class Index(generics.ListCreateAPIView,ObtainAuthToken):
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self,request,*args, **kwargs):
        print(request)    
        car = Car(placas= request.data["placas"],lat= request.data["lat"],lon= request.data["lon"],username=request.user)
        car.save()
        return Response({"msg":"Car crated succesfully"})

    def get(self,request,*args, **kwargs):
        print(request.user)    
        queryset =Car.objects.filter(username=request.user.id)
        serializer_class = CarsSerializer(queryset,many=True)
        return Response(serializer_class.data)
    
    def delete(self,request,*args, **kwargs):
        car = Car.objects.get(placas=request.data["placas"])
        car.delete()
        return Response({"msg":"car deleted"})
    
    def patch(self,request,*args, **kwargs):
        car = Car.objects.filter(placas=request.data["placas"])
        car.update(placas=request.data["newPlacas"])
        return Response({"msg":"car upadated"})
# Create your views here.

