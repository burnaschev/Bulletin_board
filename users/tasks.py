from celery import shared_task
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail


@shared_task
def send_welcome_email(user_id):
    user = get_user_model().objects.get(pk=user_id)
    subject = 'Добро пожаловать!'
    message = f'Привет {user.username},\nСпасибо за регистрацию!'
    from_email = settings.EMAIL_HOST_USER
    to_email = [user.email]

    send_mail(subject, message, from_email, to_email)
