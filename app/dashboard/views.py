from flask import Blueprint, request, render_template
from app import client

mod = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@mod.route('/')
def dashboard():
    info = client.chain_get_info()
    head_block_num = info['head_block_num']
    transaction = client.chain_get_block(head_block_num)
    get_producers = client.chain_get_producers()
    producers = sorted(get_producers['rows'], key=lambda k: k['total_votes'])
    total_vote = get_producers['total_producer_vote_weight']
    blocks = [client.chain_get_block(head_block_num)]
    for block in reversed(range(head_block_num-3, head_block_num)):
        blocks.append(client.chain_get_block(block))
    return render_template('dashboard/index.html',
                           block_num = head_block_num,
                           producers=producers,
                           total_vote=total_vote,
                           blocks=blocks)
