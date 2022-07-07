from django.contrib.auth.models import User
from django.db import models


class Tickets(models.Model):
    """Модель описывающая таски"""
    CHOISE = (
        ('a', 'Активно'),
        ('o', 'Отложено'),
        ('з', 'Закрыто'),
    )
    title = models.CharField(max_length=50, verbose_name='Название вопроса')
    content = models.TextField(verbose_name='Описание проблемы')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор тикета')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    is_active = models.CharField(max_length=1, choices=CHOISE, default='a')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Тикеты'
        verbose_name = 'Тикет'
        ordering = ['-created_at']


class Comment(models.Model):
    """Модель описывающая комментарии к таскам"""
    ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE, verbose_name='Тикет')
    author = models.CharField(max_length=50, verbose_name='Автор')
    content = models.TextField(verbose_name='Содержание')
    is_active = models.BooleanField(default=True, verbose_name='Выводить на экран?')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликован')

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'
        ordering = ['-created_at']