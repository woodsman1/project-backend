from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager

from django.contrib import admin


class UserProfilelink(models.Model):
    link = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f'{self.link}'


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    Profile_link = models.ManyToManyField(UserProfilelink)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

admin.site.register(CustomUser)
admin.site.register(UserProfilelink)