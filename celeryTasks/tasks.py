from __future__ import absolute_import, unicode_literals
from django.core.mail import send_mail
from celery import shared_task
from django.conf import settings


@shared_task
def send_notification_email(email):
    subject = 'New user created'
    message = f'Hello Samuel,\nA new user with email {email} has been created on your website.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [settings.EMAIL_HOST_USER]
    send_mail(subject, message, from_email, recipient_list, fail_silently=False,)
