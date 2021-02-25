from django.db import models

from api_reviews.validators import validate_year
from .category import Category
from .genre import Genre


class Title(models.Model):
    name = models.CharField(
        verbose_name='Имя произведения',
        help_text='Напишите здесь имя вашего произведения!',
        max_length=255,
    )
    year = models.PositiveIntegerField(
        verbose_name='Год создания произведения',
        blank=True,
        null=True,
        validators=[validate_year]
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
        related_name='titles'
    )
    category = models.ForeignKey(
        Category,
        verbose_name='Категория',
        on_delete=models.SET_NULL,
        null=True, related_name='titles'
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name
