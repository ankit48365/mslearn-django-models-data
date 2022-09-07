from .settings import *
import os


ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []
CSRF_TRUSTED_ORIGINS = ['https://'+ os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []

DATABASES = {
    "default": {
        "ENGINE": "mssql",
        "NAME": os.environ["django_db"],
        "USER": os.environ["django"],
        "PASSWORD": os.environ["P@ssword2021"],
        "HOST": os.environ["ak-az-sqlserver.database.windows.net"],
        "PORT": os.environ["1433"],
        "OPTIONS": {"driver": "ODBC Driver 17 for SQL Server", 
        },
    },
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Enables whitenoise for serving static files
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = False