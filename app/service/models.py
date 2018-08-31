from app import db

class Producer(db.Model):
    __tablename__ = 'producer_tbl'
    idx = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False)
    article = db.Column(db.Text, nullable=False)
    accnt_name = db.Column(db.String(13), nullable=False)
    slogan = db.Column(db.String(60))
    location = db.Column(db.String(60))
    homepage = db.Column(db.String(60))
    maps_lat = db.Column(db.String(20))
    maps_lng = db.Column(db.String(20))

    def __init__(self, name, email, article, accnt_name,
                 slogan=None, location=None, homepage=None, maps_lat=None,
                 maps_lng=None):
        self.name = name
        self.email = email
        self.article = article
        self.accnt_name = accnt_name
        self.slogan = slogan
        self.location = location
        self.homepage = homepage
        self.maps_lat = maps_lat
        self.maps_lng = maps_lng

    def __repr__(self):
        return '<Producer %r>' % self.name
