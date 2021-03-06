import os

import sentry_sdk

from moneycalc.settings_dev import *

DEBUG = False

ALLOWED_HOSTS = ['moneycalc.pp.ua', 'moneycalc.herokuapp.com']

SECRET_KEY = os.getenv('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.getenv('DB_HOST'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASS'),
        'PORT': os.getenv('DB_PORT'),
    }
}

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv('GOOGLE_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv('GOOGLE_SECRET')

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

sentry_sdk.init("https://8a94e87f028d4ebb88532ecb03124bb3@sentry.io/1295318")
