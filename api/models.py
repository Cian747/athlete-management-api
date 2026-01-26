from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.

class CustomUser(AbstractUser, PermissionsMixin):
  class Role(models.TextChoices):
      ADMIN, "Admin",
      COACH, "Coach",
      ATHLETE, "Athlete",

  base_role = role.ATHLETE
  role = models.CharField(max_length=50,choices=Role.choices, default=base_role)
