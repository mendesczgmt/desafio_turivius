from django.db import models
from django.contrib.auth.models import User, AbstractUser

class Profile(AbstractUser):
    email = models.CharField(max_length=133, unique=True)
    cpf = models.CharField(max_length=11)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []