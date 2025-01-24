from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # Only use True for development; set to False in production.

SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Default session backend
SESSION_COOKIE_NAME = 'sessionid'  # Default cookie name

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-^!9+@&l4d*w^^%i=k-i+ie7)$gywj+^!=*vs*s81yuj0hg5^!_"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['git-website.onrender.com', '127.0.0.1']

# Ensure the domain is correctly defined in CSRF_TRUSTED_ORIGINS
CSRF_TRUSTED_ORIGINS = ['https://git-website.onrender.com']

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Import local settings if available
try:
    from .local import *
except ImportError:
    pass

