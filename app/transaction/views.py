from flask import Blueprint, request, render_template
from flask import abort
from app import client

mod = Blueprint('transaction', __name__, url_prefix='/transaction')

@mod.route('/')
def transaction_list():
    return render_template('transaction/transaction_list.html')

@mod.route('/<tnx_id>/')
def transaction_info_from_hash(tnx_id):
    if len(tnx_id) != 64:
        abort(404)
    transaction = client.history_get_transaction(tnx_id)
    if transaction is None:
        abort(404)
    return render_template('transaction/transaction.html',
                           transaction=transaction)
