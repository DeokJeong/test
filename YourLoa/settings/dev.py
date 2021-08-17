from .base import *

# DEBUG
DEBUG = True

# ALLOWED_HOST
ALLOWED_HOSTS = ['*']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x%*n%oz#d40dd*p+h6-1uph8yhtmbo!wzmll5n5r-fy-6gp(bl'

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

CORS_ORIGIN_WHITELIST = ['http://127.0.0.1:3000' ,'http://localhost:3000']
CORS_ALLOW_CREDENTIALS = True
