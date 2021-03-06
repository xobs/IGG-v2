import os
import sys

from django.core.urlresolvers import reverse_lazy

# Import required local settings
from local_settings import DATABASES, SECRET_KEY, \
  EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_PORT, \
  EMAIL_SUBJECT_PREFIX, EMAIL_USE_TLS, SERVER_EMAIL, \
  PAYPAL_RECEIVER_EMAIL, PAYPAL_WEBSCR_URL

# Insert apps into python path
APPS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                        '../../apps'))
for path in os.listdir(APPS_DIR):
  path = os.path.join(APPS_DIR, path)
  if os.path.isdir(path):
    sys.path.insert(0, path)

IGG_ENV = os.environ.get('IGG_ENV', 'prod')

if IGG_ENV == 'dev':
  DEBUG = True
else:
  DEBUG = False

IGG_PARAM_RATE               = 0.06
IGG_PARAM_I_HR_COST          = 4.0
IGG_PARAM_DOLLARS_PER_TICKET = 5.0
IGG_PARAM_PTS_PER_MIN        = 100

IGG_PARAM_POINT_SRC_PK    = 1
IGG_PARAM_TICKET_SRC_PK   = 1
IGG_PARAM_EVENT_PK        = 1
IGG_PARAM_MARATHONINFO_PK = 1


TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Brandon Carl', 'brandon@brandoncarl.me'),
    ('Matt Rasmussen', 'matt@iggmarathon.com'),
)

# A tuple in the same format as ADMINS that specifies who should get
# broken-link notifications when SEND_BROKEN_LINK_EMAILS=True.
MANAGERS = ADMINS

# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = (
  'igg.marathon.backends.LoginUsingEmailAsUsernameBackend',
  'django.contrib.auth.backends.ModelBackend',
)

# https://docs.djangoproject.com/en/dev/topics/auth/#auth-profiles
AUTH_PROFILE_MODULE = 'marathon.UserProfile'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__),
                             '../../public/media'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__),
                              '../../public/static'))

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'igg.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'igg.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

TEMPLATE_CONTEXT_PROCESSORS = (
  'django.contrib.auth.context_processors.auth',
  'django.core.context_processors.debug',
  'django.core.context_processors.i18n',
  'django.core.context_processors.media',
  'django.core.context_processors.request', # added this
  'django.core.context_processors.static',
  'django.core.context_processors.tz',
  'django.contrib.messages.context_processors.messages',
  'igg.marathon.context.marathon_info',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # django-registration
    'registration', # registration must be above admin for correct template priority.
    'igg.marathon',
    # Admin
    'django.contrib.admin',
    # Admin documentation
    'django.contrib.admindocs',
    # django-paypal
    'paypal.standard.ipn',
)

# django-registration: https://bitbucket.org/ubernostrum/django-registration
# One-week activation window; you may, of course, use a different value.
ACCOUNT_ACTIVATION_DAYS = 7

# The URL where requests are redirected after login when the contrib.auth.login
# view gets no next parameter.
LOGIN_REDIRECT_URL = '/'

# The URL where requests are redirected for login, especially when using the
# login_required() decorator.
LOGIN_URL = reverse_lazy('auth_login')
LOGOUT_URL = reverse_lazy('auth_logout')

# Whether to send an email to the MANAGERS each time somebody visits a
# Django-powered page that is 404ed with a non-empty referer (i.e., a broken
# link). This is only used if CommonMiddleware is installed (see Middleware).
SEND_BROKEN_LINK_EMAILS = True

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
  'version': 1,
  'disable_existing_loggers': False,
  'formatters': {
    'verbose': {
      'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
    },
    'simple': {
      'format': '%(levelname)s %(message)s'
    },
  },
  'filters': {
    'require_debug_false': {
      '()': 'django.utils.log.RequireDebugFalse'
    }
  },
  'handlers': {
    'null': {
      'level':'DEBUG',
      'class':'django.utils.log.NullHandler',
    },
    'console':{
      'level':'DEBUG',
      'class':'logging.StreamHandler',
      'formatter': 'simple'
    },
    'mail_admins': {
      'level': 'ERROR',
      'filters': ['require_debug_false'],
      'class': 'django.utils.log.AdminEmailHandler'
    }
  },
  'loggers': {
    'django.request': {
      'handlers': ['mail_admins'],
      'level': 'ERROR',
      'propagate': True,
    },
    'igg.marathon': {
        'handlers': ['console', 'mail_admins'],
        'level': 'DEBUG'
    }
  }
}
