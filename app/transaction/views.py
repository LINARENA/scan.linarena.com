from flask import Blueprint, request, render_template
from flask import abort
from app.transaction.models import *
from app import client

mod = Blueprint('transaction', __name__, url_prefix='/transaction')

@mod.route('/', defaults={'page': 1})
@mod.route('/<int:page>')
def transaction_list(page):
    last_transaction = Transaction.query.order_by(Transaction.idx.desc()).first()
    if last_transaction is None:
        abort(404)
    last_page = round(last_transaction.idx / 20)
    rows_first = last_transaction.idx - (page-1)*20
    rows_last = last_transaction.idx - page*20
    transactions = Transaction.query.filter(Transaction.idx>=rows_last).\
        filter(Transaction.idx<=rows_first).order_by(Transaction.idx.desc()).all()
    return render_template('transaction/transaction_list.html',
                           page=page,
                           last_page=last_page,
                           transactions=transactions)

@mod.route('/<tnx_id>/')
def transaction_info_from_hash(tnx_id):
    if len(tnx_id) != 64:
        abort(404)
    transaction = client.history_get_transaction(tnx_id)
    if transaction is None:
        abort(404)
    return render_template('transaction/transaction.html',
                           transaction=transaction)
