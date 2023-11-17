from django.apps import AppConfig


class KiteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kite'
    path = __file__


    