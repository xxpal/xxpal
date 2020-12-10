from flask import Flask, render_template, request, escape
from vsearch import search4letters
from DBcm import UseDatabase


app = Flask(__name__)
# Use Flask built-in configuration mechanism: a dictionary to
# save database connection characteristics
app.config['dbconfig'] = {'host': '127.0.0.1',
                          'user': 'vsearch',
                          'password': 'vsearchpasswd',
                          'database': 'vsearchlogDB', }


def log_request(req: 'flask_request', res: str) -> None:
    """
    Log details of the web request and the results with the "UseDatabase" context manager
    The value of 'req' and 'res' is logged to the table 'log' of the database 'vsearchlogDB'.
    """
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """INSERT INTO log 
                  (phrase, letters, ip, browser_string, results) 
                  values 
                  (%s, %s, %s, %s, %s)"""
        cursor.execute(_SQL, (req.form['phrase'],
                              req.form['letters'],
                              req.remote_addr,
                              req.user_agent.browser,   # Extract the browser name rather than the entire strings
                              res, ))
    return


"""
1) The route decorator lets you associate a URL web path with an existing Python function.
2) The route decorator arranges for the Flask web server to call the function
   when a request for the "/" URL arrives at the server.
3) The route decorator then waits for any output produced by the decorated function before
   returning the output to the server, which then returns it to the waiting web browser.
"""


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


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


@app.route('/viewlog')
def view_the_log() -> 'html':
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """SELECT phrase, letters, ip, browser_string, results FROM log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()
    titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents, )


if __name__ == '__main__':
    app.run(debug=True)

