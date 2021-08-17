from .base import *


# DEBUG
DEBUE = False

# ALLOWED HOST
ALLOWED_HOSTS = ['*'] # will change

# SECRET KEY
SECRET_KEY = os.urandom(40)

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CORS_ORIGIN_WHITELIST = []
CORS_ALLOW_CREDENTIALS = True
