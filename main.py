from pathlib import Path
from app import app, db

if __name__ == '__main__':
    db_file = Path('./app.db')
    if not db_file.is_file():
        db.create_all()
    app.run(host='0.0.0.0', port=8080, debug=True)
