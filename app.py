from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def dashboard():
    return render_template("index.html")


# You can later add real /api/metrics endpoint
# @app.route("/api/metrics")
# def metrics():
#     import psutil, platform, datetime, random
#     return jsonify({
#         "cpu": psutil.cpu_percent(),
#         "memory": psutil.virtual_memory().percent,
#         "disk": psutil.disk_usage('/').percent,
#         ...
#     })


if __name__ == "__main__":
    app.run( port=5000)
