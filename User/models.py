
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, **extra_fields):
        """
        Создание обычного пользователя
        """
        if not email:
            raise ValueError('Email обязателен')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_unusable_password()
        user.save(using=self._db)

        return user

    def create_superuser(self, email, **extra_fields):
        """
        Создание суперпользователя
        """
        user = self.create_user(email)
        user.role = 'admin'
        user.set_unusable_password()
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
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

    username = models.CharField(
        max_length=25,
        unique=True,
        verbose_name='username',
        null=True
    )
    email = models.EmailField(
        verbose_name='Почта',
        unique=True
    )
    role = models.CharField(
        max_length=25,
        verbose_name='Роль пользователя',
        choices=Role.choices,
        default=Role.USER
    )
    bio = models.TextField(
        verbose_name='О себе',
        null=True
    )
    first_name = models.CharField(
        max_length=20,
        verbose_name='Имя',
        null=True
    )
    last_name = models.CharField(
        max_length=30,
        verbose_name='Фамилия',
        null=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    class Meta:
        ordering = ['username']
