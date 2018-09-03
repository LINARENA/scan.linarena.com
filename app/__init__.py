import json
import ast
import atexit
import time
from configparser import ConfigParser
from threading import Thread
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from resapi.res_client import ResClient


def to_pretty_json(value):
    return json.dumps(value, sort_keys=True,
                      indent=4, separators=(',', ': '))

def str_to_json(value):
    return ast.literal_eval(value)

# CONFIG JSON BEAUTIFY
# General Flask Interface section
app = Flask(__name__)
app.config.from_object('config')
app.jinja_env.filters['tojson_pretty'] = to_pretty_json
app.jinja_env.filters['str_to_json'] = str_to_json
# General SQLAlchemy Database section
db = SQLAlchemy(app)


# Blockchain Interface
client = ResClient(api_endpoint='http://211.239.124.233:19416')
config = ConfigParser()
config.read('secret_config.ini')
maps_api_js_key = config['GOOGLE']['maps_api_js_key']


# Default Flask Interface adding
@app.route('/')
def index():
    return redirect((url_for('dashboard.dashboard')), code=301)

# ErrorHandler Register section
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# database models import
from app.service.models import *
from app.block.models import *
from app.transaction.models import *
from app.action.models import *
from app.account.models import *

# Blueprint Register section
from app.dashboard.views import mod as dashboardModule
app.register_blueprint(dashboardModule)

from app.account.views import mod as accountModule
app.register_blueprint(accountModule)

from app.service.views import mod as serviceModule
app.register_blueprint(serviceModule)

from app.block.views import mod as blockModule
app.register_blueprint(blockModule)

from app.transaction.views import mod as transactionModule
app.register_blueprint(transactionModule)

from app.action.views import mod as actionModule
app.register_blueprint(actionModule)

from app.service.views import mod as serviceModule
app.register_blueprint(serviceModule)

from app.future.views import mod as futureModule
app.register_blueprint(futureModule)
