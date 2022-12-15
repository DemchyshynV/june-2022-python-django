from django.urls import path

from .views import AddCarPhotosView, CarListCreateView, CarRetrieveUpdateDestroyView

urlpatterns = [
    path('', CarListCreateView.as_view()),
    path('/<int:pk>/photo', AddCarPhotosView.as_view()),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view())

]
