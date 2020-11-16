from flask import Flask, render_template, request
from vsearch import search4letters

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'


@app.route('/search4', methods=['POST'])
def do_search() -> str:
    # Flask comes with a built-in object called 'request' to access to posted data
    # The 'request' object contains a dictionary attribute called 'form' to access to HTML form's data
    phrase = request.form['phrase']
    letters = request.form['letters']
    return str(search4letters(phrase, letters))


@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')


app.run(debug=True)

