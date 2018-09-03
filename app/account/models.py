from app import db
from sqlalchemy.dialects.mysql import BIGINT


class Account(db.Model):
    __tablename__ = 'account_tbl'
    idx = db.Column(BIGINT, primary_key=True)
    account_name = db.Column(db.String(40))
    created = db.Column(db.String(40))
    block_num = db.Column(BIGINT)

    def __init__(self, account_name, created, block_num):
        self.account_name = account_name
        self.created = created
        self.block_num = block_num

    def __repr__(self):
        return '<Account %r>' % self.account_name
