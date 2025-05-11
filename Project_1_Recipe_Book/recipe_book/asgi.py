"""
WSGI config for recipe_book project.

This file helps Django communicate with web servers using the WSGI protocol (Web Server Gateway Interface).

WSGI is a standard interface between web servers and Python web applications/frameworks like Django.

For more information, see:
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Sets the default settings module for the 'recipe_book' project
# This tells Django which settings to use when the application starts
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_book.settings')

# This is the WSGI application that the web server uses to serve your project
# It's like the entry point for handling incoming HTTP requests in a production environment
application = get_wsgi_application()
