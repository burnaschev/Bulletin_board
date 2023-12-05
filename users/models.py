from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _

NULLABLE = {'null': True, 'blank': True}


class UserRoles(models.TextChoices):
    USER = 'user', _('user')
    ADMIN = 'admin', _('admin')


class UserManager(BaseUserManager):
    """
    функция создания пользователя — в нее мы передаем обязательные поля
    """

    def create_user(self, email, first_name, last_name, phone, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            role=UserRoles.USER
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, phone, password=None):
        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password,

        )

        user.role = UserRoles.ADMIN
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = None

    first_name = models.CharField(max_length=50, verbose_name='имя')
    last_name = models.CharField(max_length=50, verbose_name='фамилия')

    phone = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='email')

    role = models.CharField(max_length=10, choices=UserRoles.choices, default=UserRoles.USER)
    image = models.ImageField(upload_to='users_img/', verbose_name='аватар', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    objects = UserManager()
