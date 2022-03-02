from uuid import uuid4
from django.db import models


class ServiceUser(models.Model):
    '''Модель пользователя сервиса To-Do'''
    uid = models.UUIDField(primary_key=True, default=uuid4)
    username = models.CharField(max_length=64)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
