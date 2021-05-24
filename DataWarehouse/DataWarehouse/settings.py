"""
Django settings for DataWarehouse project.

Generated by 'django-admin startproject' using Django 3.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-q4e6tq0k5d9fn%p&#hqr-k0lf)5l_i%k*m)^$y1fx^6gyj6y$e'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fieldAssist',
    'rest_framework',
    'drf_yasg',
    'requests'
]

REST_FRAMEWORK = {'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DataWarehouse.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
# SWAGGER_SETTINGS = {
#     "exclude_namespaces": ['rest_logout', ],  # List URL namespaces to ignore
#     "SUPPORTED_SUBMIT_METHODS": [  # Specify which methods to enable in Swagger UI
#         'get',
#         'post',
#         'put',
#         'delete'
#     ],
#     'SECURITY_DEFINITIONS': {
#         'api_key': {
#             'type': 'apiKey',
#             'in': 'header',
#             'name': 'Authorization'
#         }
#     },
#     'USE_SESSION_AUTH': True,
#     'JSON_EDITOR': True,
#     'REFETCH_SCHEMA_ON_LOGOUT': True
#
# }
WSGI_APPLICATION = 'DataWarehouse.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
          'ENGINE': 'sql_server.pyodbc',
          'NAME': 'RRKLDataWarehouse',
          'HOST': 'rrklesales.database.windows.net',
          'USER': 'esalesadmin',
          'PASSWORD': 'Ppp*12051205',
          'PORT': '1433',
          'OPTIONS': {
            'driver': 'SQL Server Native Client 11.0',
           }
         },
    'esales': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'rrklesales_2019-07-09',
        'HOST': 'rrklesales.database.windows.net',
        'USER': 'esalesadmin',
        'PASSWORD': 'Ppp*12051205',
        'PORT': '1433',
        'OPTIONS': {
            'driver': 'SQL Server Native Client 11.0',
        }
    }
 }



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
