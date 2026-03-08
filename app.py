from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)


quotes = [
    {
        "text": (
            "Success is not final, failure is not fatal: "
            "it is the courage to continue that counts."
        ),
        "author": "Winston Churchill",
    },
    {
        "text": "Believe you can and you're halfway there.",
        "author": "Theodore Roosevelt",
    },
    {
        "text": "Opportunities don't happen, you create them.",
        "author": "Chris Grosser",
    },
    {
        "text": "Dream big and dare to fail.",
        "author": "Norman Vaughan",
    },
    {
        "text": (
            "Push yourself, because no one else is going "
            "to do it for you."
        ),
        "author": "Unknown",
    },
    {
        "text": "Great things never come from comfort zones.",
        "author": "Unknown",
    },
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get-quote")
def get_quote():
    quote = random.choice(quotes)
    return jsonify(quote)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True,)



