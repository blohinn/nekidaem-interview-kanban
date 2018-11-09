from .settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_kanban',
        'USER': 'db_username',
        'PASSWORD': 'db_password',
        'HOST': 'postgres',
        'PORT': '5432',
    }
}