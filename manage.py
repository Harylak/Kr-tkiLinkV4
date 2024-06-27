#!/usr/bin/env python
"""
Narzędzie do zarządzania zadaniami administracyjnymi Django.
"""
import os
import sys

def main():
    """
    Wykonuje zadania administracyjne.
    """
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'urlshortener.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Error"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
