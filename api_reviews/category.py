from django.db import models


class Category(models.Model):
    name = models.CharField('Название')
    slug = models.SlugField('Ссылка',
                            max_length=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
