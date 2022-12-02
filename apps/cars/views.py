from rest_framework_simplejwt.authentication import JWTAuthentication

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import CarModel
from .serializers import CarSerializer

# UserModel:User = get_user_model()
# UserModel.objects.filter(userna)


class CarListCreateView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer



    def get_queryset(self):
        query = self.request.query_params.dict()

        queryset = super().get_queryset()

        if (year := query.get('lt_year')) and year.isdigit():
            queryset = queryset.filter(year__lt=year)
        if (auto_park_id := query.get('auto_park_id')) and auto_park_id.isdigit():
            queryset = queryset.filter(auto_park_id=auto_park_id)
        return queryset


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
