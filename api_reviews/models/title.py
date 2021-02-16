import datetime as dt

from django.db import models

from .category import Category
from .genre import Genre

CURENT_YEAR = dt.datetime.today().year


class Title(models.Model):
    name = models.CharField(
        verbose_name='Имя произведения',
        help_text='Напишите здесь имя вашего произведения!'
    )
    year = models.IntegerField(
        verbose_name='Год создания произведения',
        blank=True, null=True,
        max_length=4
    ) 
    description = models.TextField(
        verbose_name='Описание произведения',
        help_text='Напишите здесь описание к вашему произведению!',
        blank=True, null=True,
    )
    genre = models.ManyToManyField(
        Genre,
        related_name='title'
    )
    category = models.Choices(
        Category,
        related_name='title'
    )
    rating = models.IntegerField(
        verbose_name='Рейтинг произведения'
    )

    class Meta:
        def validate(self):
            if self.year > CURENT_YEAR:
                raise ValueError('Год не может быть больше текущего')
