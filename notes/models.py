from uuid import uuid4
from django.db import models
from service_user.models import ServiceUser


class Project(models.Model):
    '''Модель проекта для ведения заметок сервиса To-Do'''
    uid = models.UUIDField(primary_key=True, default=uuid4)
    title = models.CharField(max_length=64, verbose_name='Название проекта')
    path = models.SlugField(max_length=64, unique=True)
    users = models.ManyToManyField(ServiceUser, verbose_name='Пользователи')

    def __str__(self):
        return f'project -> {self.title}'

    class Meta:
        verbose_name = 'проект'
        verbose_name_plural = 'проекты'


class TODO(models.Model):
    '''Модель заметки сервиса To-Do'''
    uid = models.UUIDField(primary_key=True, default=uuid4)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Проект')
    content = models.TextField(max_length=5000, verbose_name='Текст заметки')
    published = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    user = models.ForeignKey(ServiceUser, on_delete=models.CASCADE, verbose_name='Автор')
    active_flag = models.BooleanField(verbose_name='Актуальность')

    def __str__(self):
        return f'To-do by {self.user} with {self.content[0:15]}'

    class Meta:
        verbose_name = 'заметка'
        verbose_name_plural = 'заметки'