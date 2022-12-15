from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.urls import path

from .views import ActivateUserView, RecoveryPasswordView, RecoveryRequestView

urlpatterns = [
    path('', TokenObtainPairView.as_view()),
    path('/refresh', TokenRefreshView.as_view()),
    path('/activate/<str:token>', ActivateUserView.as_view()),
    path('/recovery', RecoveryRequestView.as_view()),
    path('/recovery/<str:token>', RecoveryPasswordView.as_view()),

]
