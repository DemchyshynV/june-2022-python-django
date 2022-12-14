from django.core import validators as V
from django.db import models

from apps.auto_parks.models import AutoParkModel

from .managers import CarManager
from .service import upload_car_photo


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=20, unique=True, validators=[
        V.MinLengthValidator(2), V.MaxLengthValidator(20)
    ])
    year = models.IntegerField(default=2000)
    price = models.IntegerField()
    seats = models.IntegerField()
    body = models.CharField(max_length=20, blank=True)
    engine_volume = models.FloatField()
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    my_func = CarManager()


class CarPhotoModel(models.Model):
    class Meta:
        db_table = 'cars_photo'

    photo = models.ImageField(upload_to=upload_car_photo)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='photos')
