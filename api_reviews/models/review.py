from django.db import models
from .title import Title
from .user import User


class Review(models.Model):
    CHOICES = [(i, i) for i in range(1, 11)]
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
    score = models.IntegerField(
        verbose_name='Рейтинг объекта',
        help_text='Выберите рейтинг от 1 до 10',
        choices=CHOICES
    )

    class Meta:
        ordering = ('-pub_date',)

        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'], name='unique author'
            )
        ]
