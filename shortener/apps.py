from django.apps import AppConfig

class ShortenerConfig(AppConfig):
    """
    Konfiguracja aplikacji Shortener.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shortener'
