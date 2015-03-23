"""
Django settings for M3UCreator project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jiojomd88)^j8=^o=t@izhv5(ol2%xuvg#e4(f$!dqa3##)^#2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'core',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
)


ROOT_URLCONF = 'M3UCreator.urls'

WSGI_APPLICATION = 'M3UCreator.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_DIRS = (
    ('libs',os.path.join(BASE_DIR,'files','libs')),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

STATIC_ROOT = os.path.join(BASE_DIR,'files','static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR,'files','media')
MEDIA_URL = '/media/'

SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'M3U8 Creator',
    'HEADER_DATE_FORMAT': 'l, j. F Y',
    'HEADER_TIME_FORMAT': 'H:i',
    'MENU_OPEN_FIRST_CHILD': True, # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    'MENU': (
        {
            'label': 'Channels',
            'app': 'core',
            'icon': 'icon-picture',
            'models': ('channel', ),
        },
        {
            'label': 'Support',
            'app': 'core',
            'icon': 'icon-tags',
            'models': ('country','language','grouping','contenttype'),
        },
        {
            'label': 'Authentication',
            'app': 'auth',
            'icon': 'icon-lock',
            'models': ('user', 'group')
        },
    ),
    # misc
    'LIST_PER_PAGE': 25
}
