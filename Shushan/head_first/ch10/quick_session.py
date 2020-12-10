from flask import Flask, session

app = Flask(__name__)

app.secret_key = 'YouWillNeverGuess'    # Seed Flask's cookie-generation technology with a secret key


@app.route('/setuser/<user>')   # The URL needs a value (as a user) to be assigned to the "user" variable
def setuser(user: str) -> str:
    session['user'] = user  # The value of "user" is assigned to the "user" key in the "session" dictionary
    return 'User value set to: ' + session['user']


@app.route('/getuser')
def getuser() -> str:
    return 'User value is currently set to: ' + session['user']


if __name__ == '__main__':
    app.run(debug=True)
