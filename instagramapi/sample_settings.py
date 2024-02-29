from datetime import timedelta
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.postgresql',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

REST_AUTH = {
    'USE_JWT': True,
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('Bearer',),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=5),
}
ADMIN_URL = "admin"


"""Google Config"""

GOOGLE_CLOUD_TASKS_ENDPOINT = ''

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Set up email backend
GMAIL_SCOPES = 'https://mail.google.com'
GMAIL_TYPE = "service_account"
GMAIL_PROJECT_ID = ""
GMAIL_PRIVATE_KEY_ID = ""
GMAIL_PRIVATE_KEY = ""
GMAIL_CLIENT_EMAIL = ""
GMAIL_CLIENT_ID = ""
GMAIL_AUTH_URI = ""
GMAIL_TOKEN_URI = ""
GMAIL_AUTH_PROVIDER_X509_CERT_URL = ""
GMAIL_CLIENT_X509_CERT_URL = ""
GMAIL_SUBJECT = ''
