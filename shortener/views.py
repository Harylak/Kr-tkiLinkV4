from django.shortcuts import render, redirect
from .models import URL
from django.http import Http404
import re

def find_urls(text):
    """
    Znajduje wszystkie URL-e w podanym tekście
    """
    url_pattern = re.compile(r'(https?://\S+)')
    return url_pattern.findall(text)

def replace_urls(text, url_mapping):
    """
    Zastępuje URL-e w tekście ich skróconymi wersjami.
    """
    for original_url, short_url in url_mapping.items():
        text = text.replace(original_url, short_url)
    return text

def home(request):
    """
    Obsługuje żądanie strony głównej. Jeśli metoda żądania to POST, przetwarza
    wprowadzony tekst, znajduje URL, tworzy skrócone URL i zastępuje je w tekście.

    """
    if request.method == 'POST':
        original_text = request.POST.get('original_text', '')
        urls = find_urls(original_text)
        url_mapping = {}
        for original_url in urls:
            url = URL.objects.create(original_url=original_url)
            url_mapping[original_url] = request.build_absolute_uri(url.short_url)
        processed_text = replace_urls(original_text, url_mapping)
        return render(request, 'shortener/success.html', {'processed_text': processed_text})
    return render(request, 'shortener/index.html')

def redirect_url(request, short_url):
    """
    Przekierowuje do oryginalnego URL na podstawie skróconego URL.
    """
    try:
        url = URL.objects.get(short_url=short_url)
        return redirect(url.original_url)
    except URL.DoesNotExist:
        raise Http404('URL nie znaleziony')
