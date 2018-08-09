from flask import Blueprint, request, render_template
from app import client

mod = Blueprint('action', __name__, url_prefix='/action')

@mod.route('/')
def action_list():
    return render_template('action/action_list.html')

@mod.route('/hash/<action_hash>/')
def action_info_from_hash(action_hash):
    return render_template('action/action.html')
