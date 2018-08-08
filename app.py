from flask import Flask
from flask import render_template
from expiringdict import ExpiringDict
from resapi.res_client import ResClient

app = Flask(__name__)
client = ResClient(api_endpoint='http://211.239.124.233:19108')
block_list = ExpiringDict(86400, redis_hostname='127.0.0.1')

@app.route('/')
def index():
    info = client.chain_get_info()
    head_block_num = info['head_block_num']
    transaction = client.chain_get_block(head_block_num)
    get_producers = client.chain_get_producers()
    producers = sorted(get_producers['rows'], key=lambda k: k['total_votes'])
    total_vote = get_producers['total_producer_vote_weight']
    blocks = [client.chain_get_block(head_block_num)]
    for block in reversed(range(head_block_num-3, head_block_num)):
        blocks.append(client.chain_get_block(block))
    return render_template('index.html',
                           block_num = head_block_num,
                           producers=producers,
                           total_vote=total_vote,
                           blocks=blocks)

@app.route('/transactions/')
def transactions():
    return render_template('transactions.html')

@app.route('/blocks/', defaults={'page': 1})
@app.route('/users/page/<int:page>')
def blocks(page):
    info = client.chain_get_info()
    head_block_num = info['head_block_num']
    return render_template('blocks.html')

@app.route('/actions/')
def actions():
    return render_template('actions.html')

@app.route('/accounts/')
def acctouns():
    return render_template('accounts.html')

@app.route('/producers/')
def producers():
    return render_template('producers.html')

@app.route('/team/')
def team():
    return render_template('team.html')

# Comming Soon Developer
@app.route('/comming/')
def comming():
    return render_template('comming.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)
