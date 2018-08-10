from pathlib import Path
from app import app

if __name__ == '__main__':
    from app import db
    from utils.producer_insert_from_json import insert_producer
    db.create_all()
    insert_producer()
    app.run(host='0.0.0.0', port=8080, debug=True)
