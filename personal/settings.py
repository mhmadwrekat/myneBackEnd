from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DEBUG=(bool, False),
    ENVIRONMENT=(str, "PRODUCTION"),
    ALLOW_ALL_ORIGINS=(bool, False),
    ALLOWED_HOSTS=(list, []),
    ALLOWED_ORIGINS=(list, []),
    # POSTGRESQL
    DATABASE_ENGINE=(str, "django.db.backends.sqlite3"),
    DATABASE_NAME=(str, BASE_DIR / "db.sqlite3"),
    DATABASE_USER=(str, ""),
    DATABASE_PASSWORD=(str, ""),
    DATABASE_HOST=(str, ""),
    DATABASE_PORT=(int, 5432),
)

environ.Env.read_env()
ENVIRONMENT = env.str("ENVIRONMENT")
SECRET_KEY = env.str("SECRET_KEY")

DEBUG = env.bool("DEBUG")

ALLOWED_HOSTS = tuple(env.list("ALLOWED_HOSTS"))

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 3D Party Apps And Lib
    'rest_framework',
    "corsheaders",
    # in - Project apps
    'feedback',
]

MIDDLEWARE = [
    # For whitenoise : 
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    ##
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'personal.urls'

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

WSGI_APPLICATION = 'personal.wsgi.application'

## BD POSTGRESQL
DATABASES = {
    "default": {
        "ENGINE": env.str("DATABASE_ENGINE"),
        "NAME": env.str("DATABASE_NAME"),
        "USER": env.str("DATABASE_USER"),
        "PASSWORD": env.str("DATABASE_PASSWORD"),
        "HOST": env.str("DATABASE_HOST"),
        "PORT": env.int("DATABASE_PORT"),
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

#USE_L10N = True

USE_TZ = True

STATIC_URL = 'static/'
#STATIC_URL = "/static/"
#STATIC_ROOT = BASE_DIR / "staticfiles"
#AUTH_USER_MODEL = "accounts.CustomUser"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ]
}

CORS_ORIGIN_WHITELIST = tuple(env.list("ALLOWED_ORIGINS"))
CORS_ALLOW_ALL_ORIGINS = env.bool("ALLOW_ALL_ORIGINS")
