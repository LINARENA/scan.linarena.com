from flask import Blueprint, request, render_template
from flask import abort
from app.block.models import *
from app import client

mod = Blueprint('block', __name__, url_prefix='/block')


@mod.route('/', defaults={'page': 1})
@mod.route('/<int:page>')
def block_list(page):
    last_block = Block.query.order_by(Block.idx.desc()).first()
    if last_block is None:
        abort(404)
    last_page = round(last_block.idx / 20)
    rows_first = last_block.idx - (page-1)*20
    rows_last = last_block.idx -  page*20
    blocks = Block.query.filter(Block.idx>=rows_last).\
        filter(Block.idx<=rows_first).order_by(Block.idx.desc()).all()
    return render_template('block/block_list.html',
                           page=page,
                           last_page=last_page,
                           blocks=blocks)

@mod.route('/num/<block_num>/')
def block_info_from_id(block_num):
    if block_num.isnumeric() is False:
        abort(404)
    block = client.chain_get_block(block_num)
    if block is None:
        abort(404)
    return render_template('block/block.html',
                           block_num=block_num,
                           block=block)

@mod.route('/id/<block_hash>/')
def block_info_from_hash(block_hash):
    if len(block_hash) != 64:
        abort(404)
    block = client.chain_get_block(block_hash)
    if block is None:
        abort(404)
    return render_template('block/block.html',
                           block_num=block_hash,
                           block=block)
