from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'meto',
        'USER':'root',
        'PASSWORD':'root',
        'HOST':'localhost',
        'PORT':'3306',
    }
}

from django.db.backends.mysql.base import DatabaseWrapper
DatabaseWrapper.data_types['DateTimeField'] = 'datetime' # fix for MySQL 5.5

SECURE_SSL_REDIRECT = False

DEBUG = True