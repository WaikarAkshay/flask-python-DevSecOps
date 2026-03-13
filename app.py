from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def portfolio():
    # You can later pass variables to the template if needed
    context = {
        "current_year": 2026,
        "page_title": "Akshay Waikar • DevOps Engineer",
        # "visitor_count": get_visitor_count(),  # example future extension
    }
    return render_template("index.html", **context)

# Optional health check
@app.route("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
