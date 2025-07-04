from flask import Flask, jsonify
import random

app = Flask(__name__)


quotes = [
    {"author": "Albert Einstein", "quote": "Life is like riding a bicycle. To keep your balance, you must keep moving."},
    {"author": "Oscar Wilde", "quote": "Be yourself; everyone else is already taken."},
    {"author": "Maya Angelou", "quote": "You will face many defeats in life, but never let yourself be defeated."},
    {"author": "Nelson Mandela", "quote": "The greatest glory in living lies not in never falling, but in rising every time we fall."},
    {"author": "Steve Jobs", "quote": "Your time is limited, so don’t waste it living someone else’s life."}
    {"author": "Confucius", "quote": "It does not matter how slowly you go as long as you do not stop."},
    {"author": "Martin Luther King Jr.", "quote": "The time is always right to do what is right."},
    {"author": "Eleanor Roosevelt", "quote": "The future belongs to those who believe in the beauty of their dreams."},
    {"author": "Bruce Lee", "quote": "Knowing is not enough, we must apply. Willing is not enough, we must do."},
    {"author": "Malala Yousafzai", "quote": "One child, one teacher, one book, one pen can change the world."},
    {"author": "Dalai Lama", "quote": "Happiness is not something ready made. It comes from your own actions."},
    {"author": "Mark Twain", "quote": "The secret of getting ahead is getting started."},
    {"author": "Babe Ruth", "quote": "Every strike brings me closer to the next home run."}
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

