from flask import Blueprint, request, render_template
from flask import abort
from app import client

mod = Blueprint('block', __name__, url_prefix='/block')

@mod.route('/')
def block_list():
    return render_template('block/block_list.html')

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
