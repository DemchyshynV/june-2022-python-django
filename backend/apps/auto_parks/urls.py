from django.urls import path

from .views import AutoParkListCreateView, CarListCreateView

urlpatterns = [
    path('', AutoParkListCreateView.as_view(), name='auto_parks_list_create'),
    path('/<int:pk>/cars', CarListCreateView.as_view(), name='auto_parks_cars_list_create')
]
