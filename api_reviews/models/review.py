from django.db import models
from .title import Title
from .user import User


class Review(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name='Автор комментария',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    titles = models.ForeignKey(
        Title,
        verbose_name='К чему отзыв',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    parent = models.ForeignKey(
        'self',
        verbose_name='Родительский комментарий',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replies'
    )
    text = models.TextField(
        verbose_name='Текст комментария',
        help_text='Напишите здесь текст вашего комментария!',
    )
    created = models.DateTimeField(
        verbose_name='Дата создания комментария',
        auto_now_add=True
    )

    class Meta:
        ordering = ('-created',)
