from flask import Flask, render_template
import random

app = Flask(__name__)

def get_quotes():
    with open('static/quotes.txt', 'r') as file:
        quotes = file.readlines()
    return quotes

@app.route('/')
def index():
    quotes = get_quotes()
    random_quote = random.choice(quotes).strip()
    return render_template('index.html', quote=random_quote)

if __name__ == '__main__':
    app.run(debug=False, port=5005)
