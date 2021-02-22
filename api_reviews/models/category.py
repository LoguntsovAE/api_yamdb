from django.db import models


class Category(models.Model):
    name = models.CharField(
        verbose_name='Навзане категории',
        max_length=100
    )
    slug = models.SlugField(
        verbose_name='Короткий url',
        max_length=100,
        unique=True
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
