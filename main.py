from pathlib import Path
from app import app

if __name__ == '__main__':
    db_file = Path('./app.db')
    if not db_file.is_file():
        from app import db
        from producer_insert_from_json import insert_producer
        db.create_all()
        insert_producer()
    app.run(host='0.0.0.0', port=8080, debug=True)
