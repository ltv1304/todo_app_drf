from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


class ServiceUser(AbstractUser):
    '''Модель пользователя сервиса To-Do'''
    uid = models.UUIDField(primary_key=True, default=uuid4)
    first_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64, blank=True)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return f'{self.username} {self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
