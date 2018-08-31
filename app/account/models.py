from app import db
from sqlalchemy.dialects.mysql import BIGINT


class Action(db.Model):
    __tablename__ = 'action_tbl'
    idx = db.Column(BIGINT, primary_key=True)
    aciton_name = db.Column(db.String(40))
    txn_id = db.Column(db.String(64), unique=True)
    authorization = db.Column(db.String(40))
    contract = db.Column(db.String(12))

    def __init__(self, action_name, txn_id, authorization, contract):
        self.action_name = action_name
        self.txn_id = txn_id
        self.authorization = authorizaton
        self.contract = ctonract

    def __repr__(self):
        return '<Action %r>' % action_name
