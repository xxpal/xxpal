from flask import Flask     # import the Flask class from the flask module
from vsearch import search4letters


app = Flask(__name__)       # Create an instance/object of type Flask and assign it to “app” variable


"""
1) The route decorator lets you associate a URL web path with an existing Python function.
2) The route decorator arranges for the Flask web server to call the function
   when a request for the "/" URL arrives at the server.
3) The route decorator then waits for any output produced by the decorated function before
   returning the output to the server, which then returns it to the waiting web browser.
"""


@app.route('/')         # Flask's route decorator
def hello() -> str:     # Associate the URL "/" with the "hello" function
    return 'Hello World from Flask!'


@app.route('/search4')
def do_search() -> str:
    return str(search4letters('life, the universe, and everything', 'eiru,!'))


app.run()
