import datetime as dt

from django.db import models

from .category import Category
from .genre import Genre

CURENT_YEAR = dt.datetime.today().year


class Title(models.Model):
    name = models.CharField(
        verbose_name='Имя произведения',
        help_text='Напишите здесь имя вашего произведения!',
        max_length=255,
    )
    year = models.IntegerField(
        verbose_name='Год создания произведения',
        blank=True, null=True
    )
    description = models.TextField(
        verbose_name='Описание произведения',
        help_text='Напишите здесь описание к вашему произведению!',
        blank=True, null=True,
    )
    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанры',
        related_name='title'
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        null=True, related_name='title'
    )
    rating = models.IntegerField(
        verbose_name='Рейтинг произведения'
    )

    def validate(self):
        if self.year > CURENT_YEAR:
            raise ValueError('Год не может быть больше текущего')
