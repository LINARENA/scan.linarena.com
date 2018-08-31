import requests
from flask import Blueprint, request, render_template, abort
from app import client

mod = Blueprint('account', __name__, url_prefix='/account')

@mod.route('/')
def account_list():
    return render_template('account/account_list.html')

@mod.route('/<accnt_name>/', defaults={'page': 1})
@mod.route('/<accnt_name>/<int:page>')
def account_info_from_name(accnt_name, page):
    actions = client.history_get_actions(accnt_name)['actions']
    accnt_info = client.chain_get_account(accnt_name)
    if accnt_info is None:
        abort(404)
    bal_url = '/v1/chain/get_currency_balance'
    last_seq_num = actions[-1]['account_action_seq']
    last_page = round(actions[-1]['account_action_seq'] / 20)
    if page != 1:
        minus_offset = (page-1) * 20
        pos = last_seq_num - minus_offset - 20
        offset = 20
        actions = client.history_get_actions(accnt_name, pos, offset)['actions']
    currency = requests.post(client.api_endpoint+bal_url,
                             json={'code': 'eosio.token',
                                   'symbol': None,
                                   'account': accnt_name}).json()
    return render_template('account/account.html',
                           currency=currency,
                           accnt_info=accnt_info,
                           actions=actions,
                           page=page,
                           last_page=last_page)
