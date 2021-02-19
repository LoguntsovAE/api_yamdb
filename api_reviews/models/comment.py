from django.db import models

from User.models import User

from .review import Review


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        verbose_name='К чему комментарий',
        on_delete=models.CASCADE,
        related_name='comment'
    )
    text = models.CharField(
        verbose_name='Текст комментария',
        help_text='Напишите здесь текст вашего комментария!',
        max_length=255
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор комментария',
        on_delete=models.CASCADE,
        related_name='comment'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата создания отзыва',
        auto_now_add=True
    )

    class Meta:
        ordering = ('-pub_date',)
