from django.db import models

from User.models import User

from .review import Review


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        verbose_name='Ревью',
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
        related_name='comments',
        db_index=True
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата создания отзыва',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        full_name = self.author.get_full_name()
        text_comment = self.text[:30]

        return f'Автор комментария: {full_name}. Текст: {text_comment}'
