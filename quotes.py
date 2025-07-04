from flask import Flask, jsonify
import random

app = Flask(__name__)


quotes = [
    {"author": "Albert Einstein", "quote": "Life is like riding a bicycle. To keep your balance, you must keep moving."},
    {"author": "Oscar Wilde", "quote": "Be yourself; everyone else is already taken."},
    {"author": "Maya Angelou", "quote": "You will face many defeats in life, but never let yourself be defeated."},
    {"author": "Nelson Mandela", "quote": "The greatest glory in living lies not in never falling, but in rising every time we fall."},
    {"author": "Steve Jobs", "quote": "Your time is limited, so don’t waste it living someone else’s life."}
]

@app.route('/quote', methods=['GET'])
def get_quote():
    quote = random.choice(quotes)
    return jsonify(quote)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Welcome to the Quote Generator API! Visit /quote to get a random quote."
    })

if __name__ == '__main__':
    app.run(debug=True)

