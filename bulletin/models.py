from django.db import models

from config import settings

NULLABLE = {'null': True, 'blank': True}


class Ad(models.Model):
    title = models.CharField(max_length=50, verbose_name='название')
    price = models.PositiveIntegerField(default=0, verbose_name='цена')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Пользователь')
    created_at = models.DateTimeField(auto_now=True, verbose_name='дата и время создания')

    def __str__(self):
        return f'{self.title} ({self.price})'

    class Meta:
        verbose_name = 'объявление'
        verbose_name_plural = 'объявления'
        ordering = ['-created_at']


class Feedback(models.Model):
    text = models.CharField(max_length=250, verbose_name='текст')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Пользователь')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name='объявление')
    created_at = models.DateTimeField(auto_now=True, verbose_name='дата и время создания')

    def __str__(self):
        return f'{self.text}'

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
