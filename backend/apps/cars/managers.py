from django.db import models


class CarManager(models.Manager):
    def lt_seats(self, count):
        return self.filter(seats__lt=count)
