from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def check_email(self, email):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)

        return email

    def create_user(self, email, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        email = self.check_email(email)
        user = self.model(email=email, **extra_fields)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, username, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        email = self.check_email(email)
        username = self.model.normalize_username(username)
        user = self.model(
            email=email, username=username, role='admin',
            **extra_fields
        )
        user.set_password(password)
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

    email = models.EmailField(
        _('email'),
        unique=True
    )
    username = models.CharField(
        _('username'),
        max_length=30,
        unique=True,
        null=True
    )
    role = models.CharField(
        _('role'),
        max_length=30,
        choices=Role.choices,
        default=Role.USER
    )
    bio = models.TextField(
        _('bio'),
        null=True
    )
    first_name = models.CharField(
        _('first_name'),
        max_length=30,
        null=True
    )
    last_name = models.CharField(
        _('last_name'),
        max_length=40,
        null=True
    )
    is_staff = models.BooleanField(_('is_staff'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class EmailCode(models.Model):
    email = models.EmailField(
        verbose_name='Почта',
    )
    confirmation_code = models.CharField(
        verbose_name='Код подтвеждения',
        max_length=9
    )

    constraints = [
        models.UniqueConstraint(
            fields=['email', 'confirmation_code'],
            name='unique confirmation_code'
        )
    ]
