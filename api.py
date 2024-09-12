from flask import Flask, jsonify, request
from models import db, DealtCard, connect_db
import random
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('SUPABASE_DB_URL'))#, 'postgresql:///terot'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)

@app.route('/api/cards', methods=['GET'])
def get_cards():
    card_ids = request.args.getlist('ids')
    cards = DealtCard.query.filter(DealtCard.id.in_(card_ids)).all()

    result = []
    for card in cards:

        result.append({
            'name': card.card_name,
            'image_url': card.image_url,
            'description': card.description
        })

    return jsonify({'cards': result})

db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
