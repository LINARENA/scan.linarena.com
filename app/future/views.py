from flask import Blueprint, request, render_template
from app import client

mod = Blueprint('future', __name__, url_prefix='/comming')

@mod.route('/')
def comming_index():
    return render_template('future/coming.html')
