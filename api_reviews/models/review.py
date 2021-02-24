from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from User.models import User

from .title import Title


class Review(models.Model):

    author = models.ForeignKey(
        User,
        verbose_name='Автор отзыва',
        on_delete=models.CASCADE,
        related_name='reviews',
        db_index=True
    )
    title = models.ForeignKey(
        Title,
        verbose_name='Произведение',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    text = models.TextField(
        verbose_name='Текст отзыва',
        help_text='Напишите здесь текст вашего отзыва!',
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата создания отзыва',
        auto_now_add=True,
        db_index=True
    )
    score = models.PositiveSmallIntegerField(
        verbose_name='Рейтинг объекта',
        help_text='Выберите рейтинг от 1 до 10',
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'], name='unique author'
            )
        ]

    def __str__(self):
        full_name = self.author.get_full_name()
        title = self.title
        text_review = self.text[:30]
        return f'Отзыв {full_name} на произведение {title}: {text_review}'
