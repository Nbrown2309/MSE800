"""
Simple Hello Flask application.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    """Return a welcome message."""
    return "<h1>Good Morning, Flask!</h1>"

@app.route("/bye")
def bye():
    return "<h1>Goodbye, Flask!</h1>"


@app.route("/<name>/<int:number>")
def learn(name, number):
    return f"<h1>{name} is learning Flask! She wakes up at {number} o'clock in the morning.</h1>"

if __name__ == "__main__":
    app.run(debug=True)