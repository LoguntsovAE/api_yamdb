import datetime as dt

from django.core.exceptions import ValidationError
from django.db import models

from .category import Category
from .genre import Genre

CURRENT_YEAR = dt.datetime.today().year


class Title(models.Model):
    name = models.CharField(
        verbose_name='Имя произведения',
        help_text='Напишите здесь имя вашего произведения!',
        max_length=255,
    )
    year = models.PositiveIntegerField(
        verbose_name='Год создания произведения',
        blank=True, null=True
    )
    description = models.TextField(
        verbose_name='Описание произведения',
        help_text='Напишите здесь описание к вашему произведению!',
        null=True,
    )
    genre = models.ManyToManyField(
        Genre,
        blank=True,
        verbose_name='Жанры',
        related_name='genres'
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        null=True, related_name='titles'
    )

    def validate(self, year):
        if year > CURRENT_YEAR:
            raise ValidationError('Год не может быть больше текущего')
