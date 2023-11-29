from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {'null': True, 'blank': True}


class UserRoles(models.TextChoices):
    USER = 'user', _('user')
    ADMIN = 'admin', _('admin')


class User(AbstractUser):
    username = None

    first_name = models.CharField(max_length=50, verbose_name='имя')
    last_name = models.CharField(max_length=50, verbose_name='фамилия')

    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='email')

    role = models.CharField(max_length=10, choices=UserRoles.choices, default=UserRoles.USER)
    image = models.ImageField(upload_to='users_img/', verbose_name='аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

