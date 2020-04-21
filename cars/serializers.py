from rest_framework import serializers
from .models import Car

class CarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields=("placas","lat","lon","username")
        
class DeleteCarsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields=("placas")