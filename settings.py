# settings for the jsFiddle
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
path = lambda *a: os.path.join(ROOT, *a)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

# Change it to False on development machines
PRODUCTION = True

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': path('development.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        #'OPTIONS': {'init_command': 'SET storage_engine=InnoDB; SET foreign_key_checks = 0'},
        #'TEST_CHARSET': 'utf8',
        #'TEST_COLLATION': 'utf8_general_ci',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'America/Los_Angeles'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Registration
LOGIN_URL = '/account/signin/'
REGISTER_URL = '/account/signup'
LOGIN_REDIRECT_URL = '/'     # '/user/dashboard/'
REGISTER_REDIRECT_URL = '/'  # '/user/dashboard/'
AUTH_PROFILE_MODULE = 'person.Profile'

# System will look for media in these directories and use MEDIA_ROOT
# if failed
# This shouldn't be used in production. Configure WebServer to serve these
# directly from the filesystem
MEDIA_ROOTS = ()

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
# This shouldn't be used in production. Configure WebServer to serve these
# directly from the filesystem
MEDIA_ROOT = path('media')

# Place media needed to be used from apps in their media directories
APP_MEDIA_PREFIX = path('apps')
APP_MEDIA_SUFFIX = 'media'

# Where to upload the frameworks (absolute path)
#FRAMEWORKS_DIR = path('frameworks')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

STATIC_ROOT = path('static')
STATIC_URL = '/static/'

# Nose tests
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
SOUTH_TESTS_MIGRATE = False

# Django toolbar configuration
DEBUG_TOOLBAR_CONFIG = {
    # change to True needed if debugging creation of Add-ons
    'INTERCEPT_REDIRECTS': False,
}

# Switch on debug_toolbar for these IPs
INTERNAL_IPS = ('127.0.0.1',)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s '
                      '%(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s (%(name)s.%(funcName)s) %(message)s'
        },
        'syslog': {
            'format': '%(asctime)s %(levelname)s: '
                      '(%(name)s.%(funcName)s#%(lineno)d) %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'syslog': {
            'level': 'INFO',
            'class': 'logging.handlers.SysLogHandler',
            'formatter': 'syslog'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'jsf': {
            'propagate': True,
            'handlers': ['console', 'syslog'],  # , 'mail_admins'],
            'level': 'INFO',
        }
    }
}


# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
# This shouldn't be used in production. Configure WebServer to serve these
# directly from the filesystem
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'xe!+&$_&3%qahmtmt&+w)2$z8d!jul8@*_b86*qi0kcpx4hp+u'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

#TEMPLATE_CONTEXT_PROCESSORS = (
#    'django.contrib.messages.context_processors.messages',)
#
MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    path('templates'),
    # Put strings here, like "/home/html/django_templates"
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'south',
    # DEV
    'django_nose',
    'debug_toolbar',
    'lettuce.django',
    # jsFiddle APPS
    'base',
    'document',
    'source',
    'fiddle',
    'registration',
    'person',
    'library',
    # Admin
    'django.contrib.admin',
    'django.contrib.admindocs',
]

DEV_APPS = (
    'django_nose',
    'debug_toolbar',
    'lettuce.django',
)
# Which from above Middleware classes should be removed if in PRODUCTION
DEV_MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)


# Fiddle settings
FIDDLE_HASHTAG_LENGTH = 5
