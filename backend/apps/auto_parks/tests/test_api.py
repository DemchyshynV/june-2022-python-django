from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.cars.models import CarModel
from apps.users.models import UserModel as User

from ..models import AutoParkModel

UserModel: User = get_user_model()


class AutoParksTestCase(APITestCase):
    def _authenticate(self):
        email = 'admin@gmail.com'
        password = 'P@$$word1'
        self.client.post(reverse('users_list_create'), {
            "email": email,
            "password": password,
            "profile": {
                "name": "Vitaliy",
                "surname": "Demchyshyn",
                "age": 35,
                "phone": "0989542014"
            }
        }, format='json')
        user = UserModel.objects.get(email=email)
        user.is_active = True
        user.save()
        response = self.client.post(reverse('auth_login'), {"email": email, 'password': password})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {response.data["access"]}')

    def test_create_auto_park_without_auth(self):
        prev_count = AutoParkModel.objects.count()
        sample_auto_park = {
            'name': 'Uklon'
        }
        response = self.client.post(reverse('auto_parks_list_create'), sample_auto_park)
        self.assertEqual(AutoParkModel.objects.count(), prev_count)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_auto_park(self):
        self._authenticate()
        prev_count = AutoParkModel.objects.count()
        sample_auto_park = {
            'name': 'Uklon'
        }
        response = self.client.post(reverse('auto_parks_list_create'), sample_auto_park)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Uklon')
        self.assertIsInstance(response.data['cars'], list)
        self.assertEqual(AutoParkModel.objects.count(), prev_count + 1)

    def test_add_car_to_auto_park(self):
        prev_count = CarModel.objects.count()
        self._authenticate()
        sample_auto_park = {
            'name': 'Uklon'
        }
        response = self.client.post(reverse('auto_parks_list_create'), sample_auto_park)
        pk = response.data['id']
        sample_car = {
            "brand": "BMW",
            "price": 2000,
            "year": 2000,
            "seats": 5,
            "engine_volume": 2.4
        }
        cars_count = len(self.client.get(reverse('auto_parks_cars_list_create', args=(pk,))).data)
        response = self.client.post(reverse('auto_parks_cars_list_create', args=(pk,)), sample_car)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CarModel.objects.count(), prev_count + 1)
        self.assertEqual(len(response.data['cars']), cars_count + 1)
