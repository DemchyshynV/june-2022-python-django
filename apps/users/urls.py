from django.urls import path

from .views import (
    AdminToUserView,
    AutoParkListCreateView,
    UserActivateView,
    UserCreateView,
    UserDeactivateView,
    UserToAdminView,
)

urlpatterns = [
    path('', UserCreateView.as_view()),
    path('/auto_parks', AutoParkListCreateView.as_view()),
    path('/<int:pk>/activate', UserActivateView.as_view()),
    path('/<int:pk>/deactivate', UserDeactivateView.as_view()),
    path('/<int:pk>/to_admin', UserToAdminView.as_view()),
    path('/<int:pk>/to_user', AdminToUserView.as_view()),

]
