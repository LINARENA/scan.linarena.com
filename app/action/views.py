from flask import Blueprint, request, render_template, abort
from app.action.models import *
from app import client

mod = Blueprint('action', __name__, url_prefix='/action')


@mod.route('/', defaults={'page': 1})
@mod.route('/<int:page>')
def action_list(page):
    last_action = Action.query.order_by(Action.idx.desc()).first()
    if last_action is None:
        abort(404)
    last_page = round(last_action.idx / 20)
    rows_first = last_action.idx - (page-1)*20
    rows_last = last_action.idx -  page*20
    actions = Action.query.filter(Action.idx>=rows_last).\
        filter(Action.idx<=rows_first).order_by(Action.idx.desc()).all()
    return render_template('action/action_list.html',
                           page=page,
                           last_page=last_page,
                           actions=actions)

@mod.route('/hash/<action_hash>/')
def action_info_from_hash(action_hash):
    return render_template('action/action.html')
