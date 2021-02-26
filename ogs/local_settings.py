import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'groceryshop',
        'USER': 'instructor1',
        'PASSWORD': 'admin@1234'
    }
}


DEBUG = False
