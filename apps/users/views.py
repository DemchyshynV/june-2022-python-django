from rest_framework.generics import CreateAPIView

from .permissions import IsSuperUser
from .serializers import UserSerializer


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsSuperUser,)
