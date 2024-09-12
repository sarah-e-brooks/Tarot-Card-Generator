import random
import json
from models import Card, DealtCard, db

# Load JSON data from the file
with open('cards.json') as f:
    card_data = json.load(f)

# Debugging: Check the type of card_data
print(f"Type of card_data: {type(card_data)}")
print(f"Number of cards in the deck: {len(card_data)}")

class TarotDeck:
    @staticmethod
    def draw_cards(number=3):
        # Ensure card_data is a list
        if not isinstance(card_data, list):
            return {"error": "Card data should be a list of cards."}
        
        # Debugging: Print the number being requested and the length of card_data
        print(f"Requested number of cards: {number}")
        print(f"Available number of cards: {len(card_data)}")

        print("Clearing DealtCard table...")
        DealtCard.query.delete()
        db.session.commit()
        
        selected_cards = random.sample(card_data, number)
        
        # Debugging: Check the selected cards
        print(f"Selected cards: {selected_cards}")

        selected_cards = random.sample(card_data, number)
        dealt_cards = []

        for card in selected_cards:
            dealt_card = DealtCard(
                card_name=card["name"],
                image_url=card["image_url"],
                description=card["description"]
            )
            db.session.add(dealt_card)
            db.session.commit()
            dealt_cards.append(dealt_card)

        return dealt_cards