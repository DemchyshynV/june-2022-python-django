from rest_framework import status
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from .filters import CarFilter
from .models import CarModel
from .serializers import CarPhotoSerializer, CarSerializer


class CarListCreateView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    filterset_class = CarFilter

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


class AddCarPhotosView(GenericAPIView):
    queryset = CarModel.objects.all()

    def post(self, *args, **kwargs):
        files = self.request.FILES
        car = self.get_object()
        for key in files:
            serializer = CarPhotoSerializer(data={'photo': files[key]})
            serializer.is_valid(raise_exception=True)
            serializer.save(car=car)
        serializer = CarSerializer(car)
        return Response(serializer.data, status.HTTP_201_CREATED)
