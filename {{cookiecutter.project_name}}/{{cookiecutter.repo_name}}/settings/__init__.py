import os
{% if cookiecutter.languages.split(',') and cookiecutter.DjangoCMS == 'yes' %}gettext = lambda s: s{% endif %}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '_^512$1cxhgocjv*+(y9(9_f22544xk12ddnwkue4+!93o3z*#'

DEBUG = False

ALLOWED_HOSTS = [
    'localhost',
    '.elcodo.io',
]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',{% if cookiecutter.DjangoCMS == 'yes' %}
    'cms',
    'menus',
    'treebeard',{% endif %}
    'compressor',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = '{{cookiecutter.repo_name}}.urls'

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

WSGI_APPLICATION = '{{cookiecutter.repo_name}}.wsgi.application'

{% if cookiecutter.use_psql == 'yes' %}DATABASES = {
    'default': {
        'NAME': '{{cookiecutter.repo_name}}',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '',
    }
}{% endif %}
{% if cookiecutter.use_mysql == 'yes' %}DATABASES = {
    'default': {
        'NAME': '{{cookiecutter.repo_name}}',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    },
}{% endif %}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'pl'

LANGUAGES = (
    ('pl', 'pl'),
    ('en', 'en'),
)

TIME_ZONE = 'CET'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '../../static/')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '../../media/')

SITE_ID = 1

{% if cookiecutter.languages.split(',') and cookiecutter.DjangoCMS == 'yes' %}CMS_LANGUAGES = {
    1: [{% for language in cookiecutter.languages.split(',') %}
        {
            'code': '{{language}}',
            'name': gettext('{{language}}'),
            'redirect_on_fallback': True,
            'public': True,
            'hide_untranslated': False,
        },{% endfor %}
    ],
    'default': {
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
}

LANGUAGES = []
for lang in CMS_LANGUAGES[SITE_ID]:
    LANGUAGES.append((lang['code'], lang['name']))

PARLER_LANGUAGES = {
    SITE_ID: list(
        {'code': l[0]} for l in LANGUAGES
    ),
    'default': {
        'fallback': LANGUAGE_CODE,
        'hide_untranslated': True,   # the default; let .active_translations() return fallbacks too.
    }
}{% endif %}

try:
    from .local import *  # noqa
except ImportError:
    pass
