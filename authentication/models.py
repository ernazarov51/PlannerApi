from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField


# Create your models here.
class User(AbstractUser):
    phone_number=CharField(max_length=20)
