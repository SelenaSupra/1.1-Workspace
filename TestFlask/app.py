#venv/scripts/activate before working in terminal!
from flask import Flask


app = Flask(__name__)

@app.route("/")
def MyMessage():
    message = 'Hello! Here I am, guess I am your web app, and thats it...'
    return message

if __name__ == '__main__':
    app.run(debug=True)


def anotherPage():
    return 'Here is ANOTHER page, what a feat...'
