from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.user.api_rest.views import UserRegistrationView
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]