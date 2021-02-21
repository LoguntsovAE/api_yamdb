from django.db import models

from User.models import User

from .title import Title


class Review(models.Model):

    CHOICES = [(i, i) for i in range(1, 11)]

    author = models.ForeignKey(
        User,
        verbose_name='Автор отзыва',
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
        verbose_name='Текст отзыва',
        help_text='Напишите здесь текст вашего отзыва!',
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата создания отзыва',
        auto_now_add=True
    )
    score = models.PositiveSmallIntegerField(
        verbose_name='Рейтинг объекта',
        help_text='Выберите рейтинг от 1 до 10',
        choices=CHOICES
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ('-pub_date',)
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'], name='unique author'
            )
        ]

    def __str__(self):
        return 'Автор: {}. Текст: {}'.format(self.author.get_full_name(),
                                             self.text[:30])
