from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User as DUser


class Game(models.Model):
    if 'pycharm':
        DoesNotExist = None
        objects: models.manager.Manager = None

    name = models.CharField(max_length=255)
    desc = models.TextField(blank=True)
    img = models.ImageField(upload_to="images/%Y/%m/%d", blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    html = models.TextField()

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'<Game: {self} ({self.pk})>'

    def get_absolute_url(self):
        return reverse('game', kwargs={'game': self.name})

    class Meta:
        verbose_name = 'игра'
        verbose_name_plural = 'игры'
        ordering = ['name', 'time_create']


class User(models.Model):
    if 'pycharm':
        DoesNotExist = None
        objects: models.manager.Manager = None

    username = models.CharField(max_length=255)
    games_settings = models.TextField(default='{}')

    def __str__(self):
        return f'{self.username}'

    def __repr__(self):
        return f'<Game: {self} ({self.pk})>'

    def get_absolute_url(self):
        return f'/admin/auth/user/{DUser.objects.get(username=self.username).pk}/change'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
        ordering = ['username']
