from flask import Blueprint, request, render_template
from app.service.models import Producer
from app.transaction.models import Transaction
from app.action.models import Action
from app.account.models import Account
from app import client

mod = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@mod.route('/')
def dashboard():
    info = client.chain_get_info()
    head_block_num = info['head_block_num']
    transaction = client.chain_get_block(head_block_num)
    get_producers = client.chain_get_producers()
    producers = sorted(get_producers['rows'], key=lambda k: k['total_votes'])
    for idx in range(1, len(producers)+1):
        accnt_name = producers[idx-1]['owner']
        info = Producer.query.filter_by(accnt_name=accnt_name).first()
        if info is not None:
            producers[idx-1]['team'] = info.name
    total_vote = get_producers['total_producer_vote_weight']
    blocks = [client.chain_get_block(head_block_num)]
    for block in reversed(range(head_block_num-3, head_block_num)):
        blocks.append(client.chain_get_block(block))

    # Accounts
    last_account = Account.query.order_by(Account.idx.desc()).first()
    if last_account is None:
        accounts = []
    else:
        rows_first = last_account.idx - 8
        accounts = Account.query.filter(Account.idx>=rows_first).\
            filter(Account.idx<=last_account.idx).order_by(Account.idx.desc()).all()

    # Actions
    last_action = Action.query.order_by(Action.idx.desc()).first()
    if last_action is None:
        actions = []
    else:
        rows_first = last_action.idx - 8
        actions = Action.query.filter(Action.idx>=rows_first).\
            filter(Action.idx<=last_action.idx).order_by(Action.idx.desc()).all()
    count = {}
    count['trx_cnt'] = Transaction.query.count()
    count['action'] = Action.query.count()
    count['account'] = Account.query.count()
    return render_template('dashboard/index.html',
                           block_num = head_block_num,
                           producers=producers,
                           total_vote=total_vote,
                           blocks=blocks,
                           accounts=accounts,
                           actions=actions,
                           count=count)
