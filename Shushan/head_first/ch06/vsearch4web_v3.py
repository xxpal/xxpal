from flask import Flask, render_template, request, escape
from vsearch import search4letters


app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    """Log details of the web request and the results.
    The value of 'req' and 'res' is appended as on line to a file called 'vsearch.log'.
    """
    with open('vsearch.log', 'a') as log:
        print(str(dir(req)), res, file=log)


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    # Flask comes with a built-in object called 'request', which provide easy access to posted data
    # The 'request' object contains a dictionary attribute called 'form', which provides access to
    # a HTML form's data posted from the browser.
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results,)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
def view_the_log() -> str:
    with open('vsearch.log') as log:
        contents = log.read()
    # Encoding HTML's special characters so that they could appear on a webpage
    # but not be interpreted as HTML.
    return escape(contents)


if __name__ == '__main__':
    app.run(debug=True)

