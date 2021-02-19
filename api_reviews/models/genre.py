from django.db import models


class Genre(models.Model):
    name = models.CharField('Название',
                            max_length=100)
    slug = models.SlugField('Ссылка',
                            max_length=100,
                            unique=True)

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
