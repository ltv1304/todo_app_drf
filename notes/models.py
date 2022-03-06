from uuid import uuid4
from django.db import models
import service_user
from service_user.models import ServiceUser


class Project(models.Model):
    '''Модель проекта для ведения заметок сервиса To-Do'''
    uid = models.UUIDField(primary_key=True, default=uuid4)
    title = models.CharField(max_length=64)
    path = models.SlugField(max_length=64, unique=True)
    users = models.ManyToManyField(ServiceUser)

    def __str__(self):
        return f'project -> {self.title}'

    class Meta:
        verbose_name = 'проект'
        verbose_name_plural = 'проекты'


class TODO(models.Model):
    '''Модель заметки сервиса To-Do'''
    uid = models.UUIDField(primary_key=True, default=uuid4)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    content = models.TextField(max_length=5000)
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(ServiceUser, on_delete=models.CASCADE)
    active_flag = models.BooleanField()

    def __str__(self):
        return f'To-do by {self.user} with {self.content[0:15]}'

    class Meta:
        verbose_name = 'заметка'
        verbose_name_plural = 'заметки'