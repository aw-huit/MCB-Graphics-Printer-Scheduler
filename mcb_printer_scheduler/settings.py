# Django settings for mcb_printer_scheduler project.
import socket

if socket.gethostbyname(socket.gethostname()) == '140.247.195.248':
    #import config.prod as config
    import config.prod_authz_01 as config
else:
    #import config.desktop as config
    import config.desktop_authz as config
    
DEBUG = config.DEBUG
TEMPLATE_DEBUG = DEBUG

ADMINS = config.ADMINS

MANAGERS = ADMINS

DATABASES = config.DATABASES

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = config.TIME_ZONE

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

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = config.MEDIA_ROOT

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = config.MEDIA_URL

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT =  config.STATIC_ROOT

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = config.STATIC_URL

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = config.ADMIN_MEDIA_PREFIX

# Additional locations of static files
STATICFILES_DIRS = config.STATICFILES_DIRS

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = config.SECRET_KEY

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
)

ROOT_URLCONF = config.ROOT_URLCONF

TEMPLATE_DIRS = config.TEMPLATE_DIRS

INSTALLED_APPS = config.INSTALLED_APPS
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = config.LOGGING

AUTHENTICATION_BACKENDS = config.AUTHENTICATION_BACKENDS

SESSION_COOKIE_NAME = config.SESSION_COOKIE_NAME

SESSION_EXPIRE_AT_BROWSER_CLOSE = True

#LDAP_CUSTOMER_NAME = config.LDAP_CUSTOMER_NAME
#LDAP_CUSTOMER_PASSWORD = config.LDAP_CUSTOMER_PASSWORD
#LDAP_SERVER = config.LDAP_SERVER

HU_PIN_LOGIN_APP_NAME = config.HU_PIN_LOGIN_APP_NAME
HU_PIN_LOGIN_APP_NAMES = config.HU_PIN_LOGIN_APP_NAMES

SMTP_CONNECTION_STRING = 'mail.fas.harvard.edu' 
EMAIL_HOST = 'mail.fas.harvard.edu' 
SEND_BROKEN_LINK_EMAILS = True

GNUPG_HOME = config.GNUPG_HOME
GPG_PASSPHRASE = config.GPG_PASSPHRASE

MCB_GRAPHICS_EMAIL = config.MCB_GRAPHICS_EMAIL

LOGIN_URL = config.LOGIN_URL

FILE_UPLOAD_PERMISSIONS = 0644

POORMANS_DB_BACKUP_DIR = config.POORMANS_DB_BACKUP_DIR
