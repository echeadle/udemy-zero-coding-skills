from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    word_count = None
    if request.method == 'POST':
        text = request.form['text']
        words = text.split()
        word_count = len(words)
    return render_template('index.html', word_count=word_count)

if __name__ == '__main__':
    app.run(debug=False, port=5005)

