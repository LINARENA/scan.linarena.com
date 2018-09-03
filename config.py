import os
from configparser import ConfigParser

config = ConfigParser()
config.read('secret_config.ini')
_basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

# SECRET_KEY = '{{ REPLACE THIS}}'
SECRET_KEY = os.urandom(24)
if DEBUG:
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(_basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = config['LOCAL']['SQLALCHEMY_DATABASE_URI']
else:
    SQLALCHEMY_DATABASE_URI = config['GCLOUD']['SQLALCHEMY_DATABASE_URI']
SQLALCHEMY_TRACK_MODIFICATIONS = False

THREADS_PER_PAGE = 8

CSRF_ENABLED = True
CSRF_SESSION_KEY = os.urandom(24)
