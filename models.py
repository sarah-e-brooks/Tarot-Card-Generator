from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Card(db.Model):
    __tablename__ = 'cards'

    id = db.Column(db.Integer, primary_key=True)
    card_name = db.Column(db.String(50), nullable=False, unique=True)
    image_url = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200), nullable=False)

class DealtCard(db.Model):
    __tablename__ = 'dealt_cards'

    id = db.Column(db.Integer, primary_key=True)
    card_name = db.Column(db.String, nullable=False)
    image_url = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

def connect_db(app):
    """Connect this database to provided Flask app."""
    db.app = app
    db.init_app(app)
