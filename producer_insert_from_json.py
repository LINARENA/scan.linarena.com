from app.service.models import Producer
from app import db
import json


def insert_producer():
    with open('producers.json', 'r') as json_file:
        json_data = json.load(json_file)
    for data in json_data:
        producer = Producer(**data)
        db.session.add(producer)
    db.session.commit()
    return json_data

if __name__ == '__main__':
    for ret in insert_producer():
        print(ret)
