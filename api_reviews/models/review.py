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
    title = models.ForeignKey(
        Title,
        verbose_name='К чему отзыв',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField(
        verbose_name='Текст комментария',
        help_text='Напишите здесь текст вашего комментария!',
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата создания комментария',
        auto_now_add=True
    )

    class Meta:
        ordering = ('-created',)

        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'], name='unique author'
            )
        ]
