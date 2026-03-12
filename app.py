from flask import Flask, render_template, jsonify
import platform
import datetime
import random

app = Flask(__name__)

devops_tips = [
    "Automate everything you can.",
    "Monitor before scaling.",
    "Use Infrastructure as Code.",
    "Keep deployments small and frequent.",
    "Containerize your applications.",
    "Logging and observability are critical."
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/system-info")
def system_info():

    data = {
    "server": "Demo Flask Server",
    "python_version": platform.python_version(),
    "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "devops_tip": random.choice(devops_tips)
}

    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
