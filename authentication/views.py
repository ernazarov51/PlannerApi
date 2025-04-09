from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from authentication.models import User
from authentication.serializers import UserRegisterModelSerializer


# Create your views here.
class UserRegisterCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterModelSerializer

