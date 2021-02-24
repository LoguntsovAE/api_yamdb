from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Модель Юзера
    """

    class Role(models.TextChoices):
        """
        Роли
        """
        USER = 'user'
        MODERATOR = 'moderator'
        ADMIN = 'admin'

    email = models.EmailField(
        verbose_name='Почта',
        unique=True
    )
    role = models.CharField(
        verbose_name='Роль',
        max_length=30,
        choices=Role.choices,
        default=Role.USER
    )
    bio = models.TextField(
        verbose_name='О себе',
        null=True
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=30,
        null=True
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=40,
        null=True
    )

    @property
    def is_admin(self):
        return self.role == self.Role.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.is_admin or self.role == self.Role.MODERATOR

    def get_payload(self):
        return {
            'user_id': self.id,
            'email': self.email,
            'username': self.username,
        }

    class Meta:
        ordering = ('username',)
        verbose_name = 'User'
        verbose_name_plural = 'Users'
