from rest_framework.serializers import ModelSerializer

from apps.cars.serializers import CarSerializer

from .models import AutoParkModel


class AutoParkSerializer(ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = AutoParkModel
        fields = ('id', 'name', 'cars')
