from django.contrib.auth import get_user_model
from django.db import models

from apps.users.models import UserModel as User

UserModel: User = get_user_model()


class AutoParkModel(models.Model):
    class Meta:
        db_table = 'auto_parks'
        ordering = ['id']

    name = models.CharField(max_length=10)
    users = models.ManyToManyField(UserModel, through='UsersAutoParksModel', related_name='auto_parks')


class UsersAutoParksModel(models.Model):
    class Meta:
        db_table = 'cars_auto_parks'

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE)
