from app import db
from sqlalchemy.dialects.mysql import BIGINT


class Block(db.Model):
    __tablename__ = 'block_tbl'
    idx = db.Column(db.BIGINT, primary_key=True)
    block_num = db.Column(BIGINT(unsigned=True), unique=True)
    block_id = db.Column(db.String(64), unique=True)
    timestamp = db.Column(db.String(20))
    transactions = db.Column(db.Integer)
    producer = db.Column(db.String(30))

    def __init__(self, block_num, block_id, timestamp, transactions, producer):
        self.block_num = block_num
        self.block_id = block_id
        self.timestamp = timestamp
        self.transactions = transactions
        self.producer = producer

    def __repr__(self):
        return 'Block %r' % block_num
