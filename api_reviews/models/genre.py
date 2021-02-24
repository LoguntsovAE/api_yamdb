from django.db import models


class Genre(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=100
    )
    slug = models.SlugField(
        verbose_name='Короткий url',
        max_length=100,
        unique=True,
        db_index=True
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name
