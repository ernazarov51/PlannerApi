
from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from authentication.views import UserRegisterCreateAPIView

urlpatterns = [
    path('register/',UserRegisterCreateAPIView.as_view(),name='register')
]
