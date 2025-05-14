from pathlib import Path
from django.contrib.messages import constants as message_constants

BASE_DIR = Path(__file__).resolve().parent.parent

from decouple import config

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

"""
SECRET_KEY = 'django-insecure-8_!6rdwxrk&*0fnfh6bh$#mu^aau!n@^77sn=@t5@knrl$38wk'
DEBUG = False
"""
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', ]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Breach', 
    'ckeditor',
    'ckeditor_uploader',
    'django.contrib.sitemaps',
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

ROOT_URLCONF = 'Breachxpress.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
               
            ],
        },
    },
]

WSGI_APPLICATION = 'Breachxpress.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'Breach/static']
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
CKEDITOR_UPLOAD_PATH = 'uploads/'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'height': 400,
        'width': '100%',
        'toolbar_Custom': [
            ['Styles', 'Format', 'Font', 'FontSize'],
            ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
            ['TextColor', 'BGColor'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Table', 'HorizontalRule', 'SpecialChar'],
            ['Blockquote', 'CodeSnippet'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent'],
            ['Undo', 'Redo'],
            ['Source', 'Maximize'],
        ],
        'stylesSet': [{'name': 'Quote', 'element': 'span', 'attributes': {'class': 'quote'}}],
        'extraPlugins': 'codesnippet',
        'format_tags': 'p;h1;h2;h3;h4',
    },
}

DATA_UPLOAD_MAX_MEMORY_SIZE = 104857600  
FILE_UPLOAD_MAX_MEMORY_SIZE = 104857600  

MESSAGE_TAGS = {
    message_constants.SUCCESS: 'green-message',
    message_constants.ERROR: 'error-message',
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    },
}

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

