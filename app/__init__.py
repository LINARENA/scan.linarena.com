from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from resapi.res_client import ResClient

# General Flask Interface section
app = Flask(__name__)
app.config.from_object('config')

# General SQLAlchemy Database section
db = SQLAlchemy(app)


# Blockchain Interface
client = ResClient(api_endpoint='http://211.239.124.233:19108')


@app.route('/')
def index():
    return redirect((url_for('dashboard.dashboard')), code=301)

# ErrorHandler Register section
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Blueprint Register section
from app.dashboard.views import mod as dashboardModule
app.register_blueprint(dashboardModule)

