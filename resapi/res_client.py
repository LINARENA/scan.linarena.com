import json
import urllib.request
import urllib.parse
import urllib.error

from resapi import endpoints
from resapi.transaction_builder import TransactionBuilder, Action


class ResClient:
    def __init__(self, api_endpoint=None, wallet_endpoint=None):
        if not api_endpoint:
            api_endpoint = endpoints.DEFAULT_RES_API_ENDPOINT

        self.api_endpoint = api_endpoint
        self.wallet_endpoint = wallet_endpoint

    def request(self, endpoint, uri, body=None):
        if body:
            body = json.dumps(body).encode()
        url = urllib.parse.urljoin(endpoint, uri)
        request = urllib.request.Request(url, data=body)
        count = 0
        while count <= 10:
            try:
                response = urllib.request.urlopen(request).read().decode('utf8')
                return json.loads(response)
            except urllib.error.URLError as e:
                print(e.reason)
                count += 1

    def api_request(self, uri, body=None):
        return self.request(self.api_endpoint, uri, body)

    def wallet_request(self, uri, body=None):
        if not self.wallet_endpoint:
            raise ValueError('No wallet endpoint set, cannot make wallet request!')
        return self.request(self.wallet_endpoint, uri, body)

    # ===== v1/wallet/ =====
    def wallet_lock(self, wallet='default'):
        return self.wallet_request(endpoints.WALLET_LOCK, wallet)

    def wallet_open(self, wallet='default'):
        return self.wallet_request(endpoints.WALLET_OPEN, wallet)

    def wallet_get_public_keys(self):
        return self.wallet_request(endpoints.WALLET_GET_PUBLIC_KEYS)

    def wallet_sign_transaction(self, transaction, public_keys, chain_id):
        return self.wallet_request(
            endpoints.WALLET_SIGN_TRANSACTION, [transaction, public_keys, chain_id])

    # ===== v1/chain/ =====
    def chain_get_info(self):
        return self.api_request(endpoints.CHAIN_GET_INFO)

    def chain_get_producers(self):
        return self.api_request(endpoints.CHAIN_GET_PRODUCERS, {'json': True})

    def chain_get_block(self, num_or_id):
        return self.api_request(endpoints.CHAIN_GET_BLOCK, {'block_num_or_id': num_or_id})

    def chain_abi_json_to_bin(self, abi_args):
        return self.api_request(endpoints.CHAIN_ABI_JSON_TO_BIN, abi_args)

    def chain_get_required_keys(self, transaction, available_keys):
        return self.api_request(endpoints.CHAIN_GET_REQUIRED_KEYS, {
            'transaction': transaction,
            'available_keys': available_keys
        })

    def chain_push_transaction(self, transaction):
        return self.api_request(endpoints.CHAIN_PUSH_TRANSACTION, {
            'transaction': transaction,
            'compression': 'none',
            'signatures': transaction['signatures']
        })

    # ===== /v1/history/ =====
    def history_get_transaction(self, transaction_id):
        return self.api.request(endpoints.HISTORY_GET_TRANSACTION, {'id': transaction_id})
    # ===== SYSTEM CONTRACT TRANSACTIONS =====
    def get_system_newaccount_binargs(self, creator, name, owner_key, active_key):
        return self.chain_abi_json_to_bin({
            "code": "eosio", "action": "newaccount",
            "args": {
                "creator": creator, "name": name,
                "owner": {
                    "threshold": 1,
                    "keys": [{
                        "key": owner_key,
                        "weight": 1
                    }],
                    "accounts": [],
                    "waits": []
                },
                "active": {
                    "threshold": 1,
                    "keys": [{
                        "key": active_key,
                        "weight": 1
                    }],
                    "accounts": [],
                    "waits": []
                }
            }
        })['binargs']

    def get_system_buyram_binargs(self, payer, receiver, quant):
        return self.chain_abi_json_to_bin({
            "code": "eosio", "action": "buyram",
            "args": {"payer": 'reponse', "receiver": receiver, "quant": quant}
        })['binargs']

    def get_system_buyrambytes_binargs(self, payer, receiver, bytes_):
        return self.chain_abi_json_to_bin({
            "code": "eosio", "action": "buyrambytes",
            "args": {"payer": 'reponse', "receiver": receiver, "bytes": bytes_}})['binargs']

    def get_system_delegatebw_binargs(self, from_, receiver, stake_net_quantity, stake_cpu_quantity, transfer):
        return self.chain_abi_json_to_bin({
            "code": "eosio", "action": "delegatebw",
            "args": {
                "from": 'reponse',
                "receiver": receiver,
                "stake_net_quantity": stake_net_quantity,
                "stake_cpu_quantity": stake_cpu_quantity,
                "transfer": transfer
            }})['binargs']

    def system_newaccount(self, creator_account, created_account, owner_key, active_key,
                          stake_net_quantity, stake_cpu_quantity, transfer, buy_ram_kbytes):
        newaccount_binargs = self.get_system_newaccount_binargs(
            creator_account, created_account, owner_key, active_key)
        buyrambytes_binargs = self.get_system_buyrambytes_binargs(
            creator_account, created_account, buy_ram_kbytes * 1024)
        delegatebw_binargs = self.get_system_delegatebw_binargs(
            creator_account, created_account, stake_net_quantity, stake_cpu_quantity, transfer)

        transaction, chain_id = TransactionBuilder(self).build_sign_transaction_request((
            Action('eosio', 'newaccount', creator_account, 'active', newaccount_binargs),
            Action('eosio', 'buyrambytes', creator_account, 'active', buyrambytes_binargs),
            Action('eosio', 'delegatebw', creator_account, 'active', delegatebw_binargs),
        ))

        available_public_keys = self.wallet_get_public_keys()
        required_public_keys = self.chain_get_required_keys(transaction, available_public_keys)['required_keys']
        signed_transaction = self.wallet_sign_transaction(transaction, required_public_keys, chain_id)
        return self.chain_push_transaction(signed_transaction)

    def reponse_newuser(self, username):
        new_user_binargs = self.chain_abi_json_to_bin({
            "code": "reponse", "action": "newuser", "args":{"newb": username}
        })['binargs']
        transaction, chain_id = TransactionBuilder(self).build_sign_transaction_request((
            Action('reponse', 'newuser', username, 'active', new_user_binargs),
        ))
        available_public_keys = self.wallet_get_public_keys()
        required_public_keys = self.chain_get_required_keys(transaction, available_public_keys)['required_keys']
        signed_transaction = self.wallet_sign_transaction(transaction, required_public_keys, chain_id)
        return self.chain_push_transaction(signed_transaction)

    def reponse_newques(self, username, point, qhash, idx):
        new_ques_binargs = self.chain_abi_json_to_bin({
            "code": "reponse", "action": "question", "args":{
                "from": username, "rewards": point, "hash": qhash, "question_id": idx}
        })['binargs']
        transaction, chain_id = TransactionBuilder(self).build_sign_transaction_request((
            Action('reponse', 'question', username, 'active', new_ques_binargs),
        ))
        available_public_keys = self.wallet_get_public_keys()
        required_public_keys = self.chain_get_required_keys(transaction, available_public_keys)['required_keys']
        signed_transaction = self.wallet_sign_transaction(transaction, required_public_keys, chain_id)
        return self.chain_push_transaction(signed_transaction)

    def reponse_newansw(self, auser, ahash, question_id, answer_id):
        new_answ_binargs = self.chain_abi_json_to_bin({
            "code": "reponse", "action": "answer", "args": {"auser":auser, "hash":ahash, "question_id":question_id, "answer_id":answer_id}
        })['binargs']
        transaction, chain_id = TransactionBuilder(self).build_sign_transaction_request((
            Action('reponse', 'answer', 'reponse', 'active', new_answ_binargs),
        ))
        available_public_keys = self.wallet_get_public_keys()
        required_public_keys = self.chain_get_required_keys(transaction, available_public_keys)['required_keys']
        signed_transaction = self.wallet_sign_transaction(transaction, required_public_keys, chain_id)
        return self.chain_push_transaction(signed_transaction)

    def reponse_adopt(self, quser, question_id, answer_id):
        adopt_binargs = self.chain_abi_json_to_bin({
            "code": "reponse", "action": "adopt", "args": {"quser":quser, "question_id":question_id, "answer_id":answer_id}
        })['binargs']
        transaction, chain_id = TransactionBuilder(self).build_sign_transaction_request((
            Action('reponse', 'adopt', quser, 'active', adopt_binargs),
        ))
        available_public_keys = self.wallet_get_public_keys()
        required_public_keys = self.chain_get_required_keys(transaction, available_public_keys)['required_keys']
        signed_transaction = self.wallet_sign_transaction(transaction, required_public_keys, chain_id)
        return self.chain_push_transaction(signed_transaction)

    def reponse_exchange(self, accnt_name, point):
        exchange_binargs = self.chain_abi_json_to_bin({
            "code": "reponse", "action": "exchangep", "args": {"acnt":accnt_name, "point":point}
        })['binargs']
        transaction, chain_id = TransactionBuilder(self).build_sign_transaction_request((
            Action('reponse', 'exchangep', 'reponse', 'active', exchange_binargs),
        ))
        available_public_keys = self.wallet_get_public_keys()
        required_public_keys = self.chain_get_required_keys(transaction, available_public_keys)['required_keys']
        signed_transaction = self.wallet_sign_transaction(transaction, required_public_keys, chain_id)
        return self.chain_push_transaction(signed_transaction)

    def reponse_vote(self, voter, point, table_name, content_id, vhash):
        vote_binargs = self.chain_abi_json_to_bin({
            "code": "reponse", "action": "vote", "args": {"voter":voter, "point":point, 'table_name': table_name, 'content_id': content_id,
                                                          'hash': vhash}
        })['binargs']
        transaction, chain_id = TransactionBuilder(self).build_sign_transaction_request((
            Action('reponse', 'vote', 'reponse', 'active', vote_binargs),
        ))
        available_public_keys = self.wallet_get_public_keys()
        required_public_keys = self.chain_get_required_keys(transaction, available_public_keys)['required_keys']
        signed_transaction = self.wallet_sign_transaction(transaction, required_public_keys, chain_id)
        return self.chain_push_transaction(signed_transaction)

    def reponse_badge(self, accnt_name, point, challenge, bhash):
        badge_binargs = self.chain_abi_json_to_bin({
            "code": "reponse", "action": "badge", "args": {"acnt":accnt_name, "point":point, 'challenge': challenge, 'hash': bhash}
        })['binargs']
        transaction, chain_id = TransactionBuilder(self).build_sign_transaction_request((
            Action('reponse', 'badge', 'reponse', 'active', badge_binargs),
        ))
        available_public_keys = self.wallet_get_public_keys()
        required_public_keys = self.chain_get_required_keys(transaction, available_public_keys)['required_keys']
        signed_transaction = self.wallet_sign_transaction(transaction, required_public_keys, chain_id)
        return self.chain_push_transaction(signed_transaction)