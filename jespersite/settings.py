"""
Django settings for jespersite project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-12jfma1_84e5a12!d%a+yz(coesh_73-b=2)^3j14&pur6dant'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['mysite.com', '127.0.0.1']


# установленные приложения в нашем пакете
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainapp.apps.MainappConfig',
    'uuslug',
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'social_django.middleware.SocialAuthExceptionMiddleware', #debug false
]

ROOT_URLCONF = 'jespersite.urls'

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

                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = (    
    'django.contrib.auth.backends.ModelBackend',    # бекенд классической аутентификации
    'social_core.backends.email.EmailAuth',
    'social_core.backends.google.GoogleOAuth2',     # бекенд авторизации через google
    'social_core.backends.telegram.TelegramAuth',   # бекенд авторизации через telegram
    'social_core.backends.vk.VKOAuth2',             # бекенд авторизации через VK
)

#SOCIAL_AUTH_EMAIL_FORM_URL = '/login-form/'
#SOCIAL_AUTH_EMAIL_FORM_HTML = 

# Google Consumer Key
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '404096088666-7q3l3p5r0ts1mkh31ta9flhep2jkpe49.apps.googleusercontent.com'
# Google Consumer Secret
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

SOCIAL_AUTH_TELEGRAM_BOT_TOKEN = '5777561664:AAEM6PVmJ689eUbSQXtHO4z502u0HDNCc5M'

SOCIAL_AUTH_VK_OAUTH2_KEY = '51474603'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'AYwPymlZbqaQkNeFZaU4'
SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['email']


# перенаправление при успешной авторизации
LOGIN_REDIRECT_URL = '/'

WSGI_APPLICATION = 'jespersite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_USER_MODEL = 'mainapp.MyUser'

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
# обеспечение корректной работы перемещения всех стат. ф. перед deploy

# префикс url адреса для статических файлов
STATIC_URL = '/static/'
# путь к общей статической папке web сервера
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# список нестандартных путей к статическим файлам
STATICFILES_DIRS = []

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# формирование пути к каталогу media
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# префикс url адреса для медиа  файлов
MEDIA_URL = '/media/'
