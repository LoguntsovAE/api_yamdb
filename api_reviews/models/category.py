from django.db import models


class Category(models.Model):
    name = models.CharField(
        verbose_name='Название категории',
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
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
