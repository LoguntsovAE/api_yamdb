from django.db import models

from User.models import User

from .review import Review


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        verbose_name='К чему комментарий',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField(
        verbose_name='Текст комментария',
        help_text='Напишите здесь текст вашего комментария!',
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор комментария',
        on_delete=models.CASCADE,
        related_name='comments'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата создания отзыва',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('-pub_date',)

    def __str__(self):
        return 'Автор комментария: {}. Текст: {}'.format(
            self.author.get_full_name(),
            self.text[:30]
        )
