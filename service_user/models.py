from uuid import uuid4
from django.db import models


class ServiceUser(models.Model):
    '''Модель пользователя сервиса To-Do'''
    uid = models.UUIDField(primary_key=True, default=uuid4)
    user_name = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f'{self.user_name} {self.email}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
