"""
ASGI config for elsys_chess_app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
# import channels.layers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'elsys_chess_app.settings')

application = get_asgi_application()
# channel_layer = channels.layers.get_channel_layer()
