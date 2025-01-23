from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-^!9+@&l4d*w^^%i=k-i+ie7)$gywj+^!=*vs*s81yuj0hg5^!_"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = (['git-website.onrender.com'])
#ALLOWED_HOSTS = ["*"]
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
