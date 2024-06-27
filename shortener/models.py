from django.db import models
import string
import random

class URL(models.Model):
    """
    Model reprezentujący URL i jego skróconą wersję.
    """
    original_url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True, blank=True)

    def save(self, *args, **kwargs):
        """
        Nadpisuje metodę save, aby wygenerować skrócony URL, jeśli nie istnieje.
        """
        if not self.short_url:
            self.short_url = self.generate_short_url()
        super(URL, self).save(*args, **kwargs)

    def generate_short_url(self):
        """
        Generuje unikalny skrócony URL za pomocą losowych znaków.
        """
        length = 6
        characters = string.ascii_letters + string.digits
        while True:
            short_url = ''.join(random.choice(characters) for _ in range(length))
            if not URL.objects.filter(short_url=short_url).exists():
                break
        return short_url

    def __str__(self):
        """
        Zwraca reprezentację tekstową obiektu URL.
        """
        return f'{self.original_url} -> {self.short_url}'
