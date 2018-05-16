from moneycalc.settings_dev import *

DEBUG = False

ALLOWED_HOSTS = ['moneycalc.pp.ua']

SECRET_KEY = SECRET_DATA['secret_key']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': SECRET_DATA['database']['host'],
        'NAME': SECRET_DATA['database']['name'],
        'USER': SECRET_DATA['database']['name'],
        'PASSWORD': SECRET_DATA['database']['password'],
        'PORT': SECRET_DATA['database']['port'],
    }
}