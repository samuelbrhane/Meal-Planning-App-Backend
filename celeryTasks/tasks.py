from __future__ import absolute_import, unicode_literals
from django.core.mail import send_mail
from celery import shared_task
from django.conf import settings


# new user created email notification
@shared_task
def account_created_notification_email(email):
    subject = 'New user created notification'
    message = f'Hello Samuel,\nA new user with email {email} has been created on your website.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [settings.EMAIL_HOST_USER]
    send_mail(subject, message, from_email, recipient_list, fail_silently=False,)
    

# a new meal plan created notification
@shared_task
def meal_created_notification_email(email, selectedDate):
    subject = 'Meal plan created notification'
    message = f'Hello Samuel,\nA user with email {email} has created a new meal plan for {selectedDate}.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [settings.EMAIL_HOST_USER]
    send_mail(subject, message, from_email, recipient_list, fail_silently=False,)
    

# a meal plan deleted notification
@shared_task
def meal_deleted_notification_email(email, selectedDate):
    subject = 'Meal plan deleted notification'
    message = f'Hello Samuel,\nA user with email {email} has deleted a meal plan for {selectedDate}.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [settings.EMAIL_HOST_USER]
    send_mail(subject, message, from_email, recipient_list, fail_silently=False,)
 

# a meal plan updated notification  
@shared_task
def meal_updated_notification_email(email, selectedDate):
    subject = 'Meal plan updated notification'
    message = f'Hello Samuel,\nA user with email {email} has updated a meal plan for {selectedDate}.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [settings.EMAIL_HOST_USER]
    send_mail(subject, message, from_email, recipient_list, fail_silently=False,)
