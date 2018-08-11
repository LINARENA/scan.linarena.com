from flask import Blueprint, request, render_template, abort
from app.service.models import Producer
from app import client, db
from app import maps_api_js_key

mod = Blueprint('service', __name__, url_prefix='/service')

@mod.route('/team/')
def team():
    return render_template('service/team.html')

@mod.route('/producer/')
def producer_list():
    get_producers = client.chain_get_producers()
    producers = sorted(get_producers['rows'], key=lambda k: k['total_votes'])
    for idx in range(1, len(producers)+1):
        accnt_name = producers[idx-1]['owner']
        info = Producer.query.filter_by(accnt_name=accnt_name).first()
        if info is not None:
            producers[idx-1]['homepage'] = info.homepage
            producers[idx-1]['loc'] = info.location
            producers[idx-1]['team'] = info.name
        else:
            producers[idx-1]['homepage'] = 'Comming Soon'
            producers[idx-1]['loc'] = 'Comming Soon'
            producers[idx-1]['team'] = 'Comming Soon'
    total_vote = get_producers['total_producer_vote_weight']
    return render_template('service/producer_list.html',
                           producers=producers, total_vote=total_vote)

@mod.route('/producer/<name>')
def producer(name):
    producer = Producer.query.filter_by(name=name).first()
    if producer is None:
        abort(404)
    return render_template('service/producer.html',
                           producer=producer,
                           maps_api_js_key=maps_api_js_key)
