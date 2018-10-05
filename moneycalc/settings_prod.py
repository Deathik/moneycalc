import os

from moneycalc.settings_dev import *

DEBUG = False

ALLOWED_HOSTS = ['moneycalc.pp.ua']

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
