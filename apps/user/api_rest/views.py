from rest_framework.permissions import AllowAny
from rest_framework import generics
from .serializers import UserRegistrationSerializer

class UserRegistrationView(generics.CreateAPIView):
    """
    View para registro de novos usuários.

    """
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
