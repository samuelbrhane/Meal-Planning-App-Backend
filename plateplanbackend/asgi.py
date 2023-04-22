"""
ASGI config for plateplanbackend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from .consumers import MealUsers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'plateplanbackend.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter([
        path('ws/meal/', MealUsers.as_asgi()),
    ])
})
