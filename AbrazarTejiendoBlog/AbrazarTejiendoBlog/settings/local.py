from .base import *

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'BlogAbrazarTejiendo',
        'USER':'root',
        'PASSWORD': '',
        'HOST':'localhost',
        'PORT':'3306'
    }
}