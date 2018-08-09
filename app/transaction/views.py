from flask import Blueprint, request, render_template
from app import client

mod = Blueprint('transaction', __name__, url_prefix='/transaction')

@mod.route('/')
def transaction_list():
    return render_template('transaction/transaction_list.html')

@mod.route('/hash/<block_hash>/')
def transaction_info_from_hash(transaction_hash):
    return render_template('transaction/transaction.html')
