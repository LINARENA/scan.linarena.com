from app import db
from sqlalchemy.dialects.mysql import BIGINT


class Transaction(db.Model):
    __tablename__ = 'transaction_tbl'
    idx = db.Column(BIGINT, primary_key=True)
    txn_id = db.Column(db.String(64), unique=True)
    timestamp = db.Column(db.String(40))
    actions = db.Column(db.Integer)
    block_id = db.Column(db.String(64))

    def __init__(self, txn_id, timestamp, actions, block_id):
        self.txn_id = txn_id
        self.timestamp = timestamp
        self.actions = actions
        self.block_id = block_id

    def __repr__(self):
        return 'Transaction %r' % self.txn_id
