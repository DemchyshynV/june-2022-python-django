from django.contrib.auth import get_user_model
from django.db import models

from apps.users.models import UserModel as User

UserModel: User = get_user_model()

class AutoParkModel(models.Model):
    class Meta:
        db_table = 'auto_parks'

    name = models.CharField(max_length=10)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='auto_parks')
