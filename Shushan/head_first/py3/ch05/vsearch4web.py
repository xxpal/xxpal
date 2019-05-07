from flask import Flask, render_template, request, escape
from vsearch import search4letters
import mysql.connector  # Import the driver

app = Flask(__name__)


"""
1) The route decorator lets you associate a URL web path with an existing Python function.
2) The route decorator arranges for the Flask web server to call the function
   when a request for the "/" URL arrives at the server.
3) The route decorator then waits for any output produced by the decorated function before
   returning the output to the server, which then returns it to the waiting web browser.
"""
# @app.route('/')         # Flask's route decorator
# def hello() -> '302':     # Associate the URL "/" with the "hello" function
#     # return 'Hello World from Flask!'
#     return redirect('/entry')


def log_request(req: 'flask_request', res: str) -> None:
    """Log details of the web request and the results."""
    # with open('vsearch.log', 'a') as log:
    #     # print(req, res, file=log)
    #     # print(str(dir(req)), res, file=log)
    #     # print(req.form, file=log, end='|')
    #     # print(req.remote_addr, file=log, end='|')
    #     # print(req.user_agent, file=log, end='|')
    #     # print(res, file=log)
    #     print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')

    # Define the connection characteristics
    dbconfig = {'host': '127.0.0.1',
                'user': 'vsearch',
                'password': 'vsearchpasswd',
                'database': 'vsearchlogDB', }
    conn = mysql.connector.connect(**dbconfig)  # Establish a connection
    cursor = conn.cursor()  # Create a cursor
    # Create a string containing the query you want to use
    _SQL = """insert into log 
              (phrase, letters, ip, browser_string, results)
              values 
              (%s, %s, %s, %s, %s)"""
    # Execute the query
    cursor.execute(_SQL, (req.form['phrase'],
                          req.form['letters'],
                          req.remote_addr,
                          req.user_agent.browser,
                          res,))
    conn.commit()
    cursor.close()
    conn.close()


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    # Flask comes with a built-in object called request, which provide easy access to posted data
    # The request object contains a dictionary attribute called form, which provides access to
    # a HTML form's data posted from the browser.
    title = 'Here are your results:'
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_title=title,
                           the_phrase=phrase,
                           the_letters=letters,
                           the_results=results)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the web!')


@app.route('/viewlog')
# def view_the_log() -> str:
def view_the_log() -> 'html':
    # read all contents in one go and return the string
    # with open('vsearch.log') as log:
    #     contents = log.read()
    # return escape(contents)

    # read contents by line and then be joined to one large string and return
    # with open('vsearch.log') as log:
    #     contents = log.readlines()
    # return escape(''.join(contents))

    # read contents and convert them to list of lists, then return
    contents = []
    with open('vsearch.log') as log:
        for line in log:            # Loop through each line in the "log" file stream
            contents.append([])     # Append a new, empty list to "contents"
            # Split the line (| as delimiter), then process each item
            for item in line.split('|'):
                contents[-1].append(escape(item))
    # Create a tuple of descriptive titles
    titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')

    # return str(contents)
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,)


if __name__ == '__main__':
    app.run(debug=True)

# app.run()

#
#
# app = Flask(__name__)
#
#
# # @app.route('/')
# # def hello() -> '302':
# #     return redirect('/entry')
#
# # The function to log request in a file
# # def log_request(req: 'flask_request', res: str) -> None:
# #     with open('vsearch.log', 'a') as log:
# #         print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')
#
#
# # The function to log request in a table of DB.
# def log_request(req: 'flask_request', res: str) -> None:
#     dbconfig = {'host': '127.0.0.1',
#                 'user': 'vsearch',
#                 'password': 'vsearchpasswd',
#                 'database': 'vsearchlogDB', }
#     import mysql.connector
#     conn = mysql.connector.connect(**dbconfig)
#     cursor = conn.cursor()
#     _SQL = """insert into log
#               (phrase, letters, ip, browser_string, results)
#               values
#               (%s, %s, %s, %s, %s)"""
#     cursor.execute(_SQL, (req.form['phrase'],
#                           req.form['letters'],
#                           req.remote_addr,
#                           req.user_agent.browser,
#                           res, ))
#     conn.commit()
#     cursor.close()
#     conn.close()
#
#
# @app.route('/search4', methods=['POST'])
# def do_search() -> 'html':
#     phrase = request.form['phrase']
#     letters = request.form['letters']
#     title = 'Here are your results:'
#     results = str(search4letters(phrase, letters))
#     log_request(request, results)
#     return render_template('results.html',
#                            the_phrase=phrase,
#                            the_letters=letters,
#                            the_title=title,
#                            the_results=results)
#
#
# @app.route('/')
# @app.route('/entry')
# def entry_page() -> 'html':
#     return render_template('entry.html',
#                            the_title='Welcome to search4letters on the web!')
#
#
# @app.route('/viewlog')
# # def view_the_log() -> 'str':
# #     contents = []
# #     with open('vsearch.log') as log:
# #         for line in log:
# #             contents.append([])
# #             for item in line.split('|'):
# #                 contents[-1].append(escape(item))
# #     return str(contents)
# def view_the_log() -> 'html':
#     contents = []
#     with open('vsearch.log') as log:
#         for line in log:
#             contents.append([])
#             for item in line.split('|'):
#                 contents[-1].append(escape(item))
#     titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
#     return render_template('viewlog.html',
#                            the_title='View Log',
#                            the_row_titles=titles,
#                            the_data=contents,)
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
