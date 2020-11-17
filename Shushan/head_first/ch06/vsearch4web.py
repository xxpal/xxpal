from flask import Flask, render_template, request, escape
from vsearch import search4letters


app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    """
    Log details of the web request and the results.
    The value of 'req' and 'res' is appended as one line to a file called 'vsearch.log'.
    """
    with open('vsearch.log', 'a') as log:
        # Log each web request in a single line,
        # and with a vertical bar delimiting each logged data item.
        # Print 4 items in one call with 'sep' argument.
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')


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
    contents = []   # Create a new empty list to store logs as list of lists
    with open('vsearch.log') as log:
        # Loop through each line in the "log" file stream
        for line in log:
            contents.append([])     # Append a new, empty list to "contents"
            # Split each line (| as the delimiter), then process each item in the resulting "split list"
            for item in line.split('|'):
                # Append the escaped data to the end of the list at the end of "contents"
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')  # Create a tuple of descriptive titles
    # Call "render_template", providing values for each of the template's arguments
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,)


if __name__ == '__main__':
    app.run(debug=True)

