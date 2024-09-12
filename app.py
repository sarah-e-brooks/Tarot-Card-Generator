import os
from flask import Flask, render_template, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy import text
from flask_migrate import Migrate
from models import db, Card, DealtCard, connect_db
from tarot_deck import TarotDeck
import requests
import random

app = Flask(__name__)

# Configuration settings
app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('SUPABASE_DB_URL')) #, 'postgresql:///terot'))
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False  # Typically False, prevents toolbar from interfering with redirects
app.config['SECRET_KEY'] = os.urandom(24)

# db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Initialize Debug Toolbar
toolbar = DebugToolbarExtension(app)

# Connect and initialize the database
connect_db(app)

# Initialize the Tarot deck
deck = TarotDeck()

# Define routes
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/draw_cards', methods=['GET'])
def draw_cards():
    # Use the TarotDeck class to draw cards
    dealt_cards = deck.draw_cards(3)
    
    # If the deck has fewer cards than requested
    if "error" in dealt_cards:
        return jsonify(dealt_cards), 400

    return render_template('draw_cards.html', dealt_cards=dealt_cards)

@app.route('/test_db_connection')
def test_db_connection():
    try:
        db.session.execute(text('SELECT 1'))
        return "Database connection successful!"
    except Exception as e:
        return f"Error connecting to the database: {e}"


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
