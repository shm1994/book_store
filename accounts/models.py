from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractUser , AbstractBaseUser

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(default=18, validators=[MinValueValidator(18)] , null = True , blank = True)
