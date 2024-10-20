from datetime import datetime
from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# =================== ENVIRONMENT VARIABLES =================== #
from dotenv import load_dotenv
env_file = BASE_DIR / ".env"
load_dotenv(env_file)

# =
if not env_file.exists():
    env_file_data = {}
    env_file_data["DB_NAME"] = os.environ.get("DB_NAME")
    env_file_data["DB_USER"] = os.environ.get("DB_USER")
    env_file_data["DB_PASSWORD"] = os.environ.get("DB_PASSWORD")
    env_file_data["DB_HOST"] = os.environ.get("DB_HOST")
    env_file_data["DB_PORT"] = os.environ.get("DB_PORT")
    
    env_file.write_text("\n".join([f"{k}={v}" for k, v in env_file_data.items()]))


SECRET_KEY = 'django-insecure-c)wlux^_wzyx1^8m9da99%gjt!2y$$6=_&n^9&k_65k=q44bhg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# =================== ALLOWED HOSTS =================== #
ALLOWED_HOSTS = ['*']
 
# =================== CSRF TRUSTED ORIGINS =================== #
CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:8000', 'http://localhost:8000']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # =================== MY APP =================== #
    "myapp",
    # =================== CRON TAB =================== #
     'django_crontab',
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

ROOT_URLCONF = 'mysite.urls'

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

WSGI_APPLICATION = 'mysite.wsgi.application'


# =================== DATABASES =================== #
postgres_con =   {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT"),
    }
sqlite_con = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
is_sqlite = os.environ.get("DB_HOST") is  None

DATABASES = {
    'default': sqlite_con if is_sqlite else postgres_con
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

USE_TZ = True


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


STATIC_URL = 'static/'

# =================== STATIC FILES =================== #
STATIC_ROOT = BASE_DIR / 'staticfiles'


# =================== LOGGING =================== #

today = datetime.now().strftime("%Y-%m-%d")

file_path = BASE_DIR / "DEBUG_LOGS" / f"{today}_Logs"
file_path.mkdir(parents=True, exist_ok=True)

APP_LOG_FILENAME = file_path / f"debug_{today}.log"
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {"format": "%(asctime)-8s %(name)-8s %(levelname)-8s %(message)s"},
        "file": {"format": "%(asctime)-8s %(levelname)-8s %(message)s"},
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "console"},
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "formatter": "file",
            "filename": APP_LOG_FILENAME,
            "encoding": "utf-8",
        },
    },
    "loggers": {
        "": {"level": "INFO", "handlers": [
            "file",
            "console"
        ]},
    },
}

# =================== CRONJOBS =================== #

CRONJOBS = [
    ('*/1 * * * *', 'myapp.cron.my_scheduled_job')
]