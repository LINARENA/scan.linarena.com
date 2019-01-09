from app.service.models import *
from app.block.models import *
from app.transaction.models import *
from app.action.models import *
from app.account.models import *
from app import client
from app import db
import time
import json

from app.service.models import Producer
from app import client, db
from app import maps_api_js_key

def block_parse():
    try:
        while True:
            loc_last_block = Block.query.order_by(Block.block_num.asc()).all()
            if len(loc_last_block) == 0:
                current_block = 0
            else:
                current_block = loc_last_block[-1].block_num
            parse_last_block = client.chain_get_info()['head_block_num']
            sync_count = 0
            while current_block < parse_last_block and sync_count < 100:
                current_block += 1
                block_info = client.chain_get_block(current_block)
                block_num = block_info['block_num']
                block_id = block_info['id']
                timestamp = block_info['timestamp']
                transactions = len(block_info['transactions'])
                producer = block_info['producer']
                block = Block(block_num, block_id, timestamp, transactions, producer)
                db.session.add(block)
                if transactions != 0:
                    # Block info in transactions information, add transactions
                    for transaction in block_info['transactions']:
                        txn_id = transaction['trx']['id']
                        expiration = transaction['trx']['transaction']['expiration']
                        actions = transaction['trx']['transaction']['actions']
                        trx = Transaction(txn_id, timestamp, len(actions), block_num)
                        db.session.add(trx)
                        if len(actions) != 0:
                            acts, accounts = action_parse(txn_id)
                            for act in acts:
                                db.session.add(act)
                            for account in accounts:
                                db.session.add(account)
                db.session.commit()
                sync_count += 1
                # Sleep for node chain performance
                time.sleep(0.5)
            if sync_count < 100:
                time.sleep(10)
            else:
                time.sleep(5)
    except Exception as e:
        print(e)


def action_parse(txn_id):
    act_data = client.history_get_transaction(txn_id)
    actions = act_data['trx']['trx']['actions']
    ret_action = []
    ret_account = []
    for action in actions:
        action_name = action['name']
        authorization = action['authorization'][-1]
        contract = action['account']
        act = Action(action_name, txn_id, str(authorization), contract)
        ret_action.append(act)
        if action_name == 'newaccount' and contract == 'eosio':
            account_name = action['data']['name']
            created = act_data['block_time']
            block_num = act_data['block_num']
            account = Account(account_name, created, block_num)
            ret_account.append(account)
    return ret_action, ret_account
