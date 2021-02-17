from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, **extra_fields):
        """
        Создание и сохранение юзера с данными параметрами
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_user(self, email, **extra_fields):
        """
        Создание обычного пользователя
        """
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, **extra_fields)

    def create_superuser(self, email, **extra_fields):
        """
        Создание суперпользователя
        """
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Модель Юзера
    """
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(
        _('first name'),
        max_length=30,
        blank=True,
        unique=True
    )
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    description = models.CharField(
        _('description'), max_length=200, blank=True
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Возвращает first_name и last_name в качестве полного имени
        """
        full_name = f'{self.first_name} {self.last_name}'
        return full_name.strip()

    def get_short_name(self):
        """
        Возвращает в качестве короткого имени first_name
        """
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Как будет происходить отправка имейла
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
