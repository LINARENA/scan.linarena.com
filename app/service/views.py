from flask import Blueprint, request, render_template
from app import client

mod = Blueprint('service', __name__, url_prefix='/service')

@mod.route('/team/')
def team():
    return render_template('service/team.html')

@mod.route('/producers/')
def producers():
    return render_template('service/producers.html')
