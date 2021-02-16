from django.db import models

from .category import Category
from .genre import Genre


class Title(models.Model):
    name = models.CharField('Название',
                            max_length=255)
    author = models.CharField('Автор',
                              max_length=100)
    year = models.IntegerField('Год',
                               max_length=4)
    description = models.TextField('Описание')
    genres = models.ManyToManyField(Genre,
                                    verbose_name='Жанры')
    category = models.ForeignKey(Category,
                                 verbose_name='Категория',
                                 on_delete=models.SET_NULL,
                                 null=True)

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'
