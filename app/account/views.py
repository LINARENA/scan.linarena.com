from flask import Blueprint, request, render_template
from app import client

mod = Blueprint('account', __name__, url_prefix='/account')

@mod.route('/')
def account_list():
    return render_template('account/account_list.html')

@mod.route('/<accnt_name>/')
def account_info_from_name(accnt_name):
    name = accnt_name
    return render_template('account/account.html')
