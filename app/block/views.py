from flask import Blueprint, request, render_template
from app import client

mod = Blueprint('block', __name__, url_prefix='/block')

@mod.route('/')
def block_list():
    return render_template('block/block_list.html')

@mod.route('/id/<block_id>/')
def block_info_from_id(block_id):
    return render_template('block/block.html')

@mod.route('/hash/<block_hash>/')
def block_info_from_hash(block_hash):
    return render_template('block/block.html')
