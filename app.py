from flask import Flask, render_template, jsonify
import os
import socket
import time
from datetime import datetime

app = Flask(__name__)

# Track uptime
start_time = time.time()

# Environment variables
APP_VERSION = os.getenv("APP_VERSION", "v1.0.0")
ENVIRONMENT = os.getenv("ENVIRONMENT", "Production")
HOSTNAME = socket.gethostname()


# -----------------------------
# HOME
# -----------------------------
@app.route('/')
def home():
    uptime_seconds = int(time.time() - start_time)

    return render_template(
        'index.html',
        version=APP_VERSION,
        environment=ENVIRONMENT,
        hostname=HOSTNAME,
        uptime=uptime_seconds
    )


# -----------------------------
# HEALTH CHECK
# -----------------------------
@app.route('/health')
def health():
    return jsonify({
        "status": "UP",
        "service": "devsecops-flask-app",
        "version": APP_VERSION,
        "environment": ENVIRONMENT,
        "hostname": HOSTNAME,
        "timestamp": datetime.utcnow().isoformat()
    }), 200


# -----------------------------
# METRICS (Prometheus)
# -----------------------------
@app.route('/metrics')
def metrics():
    uptime_seconds = int(time.time() - start_time)

    return f"""
# HELP app_uptime_seconds Application uptime
# TYPE app_uptime_seconds counter
app_uptime_seconds {uptime_seconds}

# HELP app_info Application Info
# TYPE app_info gauge
app_info{{version="{APP_VERSION}", environment="{ENVIRONMENT}"}} 1
""", 200, {'Content-Type': 'text/plain'}


# -----------------------------
# PIPELINE INFO API
# -----------------------------
@app.route('/pipeline')
def pipeline():
    return jsonify({
        "Code Quality": ["Flake8", "Bandit"],
        "Secrets Scan": ["Gitleaks"],
        "Dependency Scan": ["pip-audit"],
        "Container": ["Hadolint", "Trivy"],
        "Deployment": ["DockerHub", "EC2 SSH (appleboy)"]
    })


# -----------------------------
# INFO
# -----------------------------
@app.route('/info')
def info():
    return jsonify({
        "project": "End-to-End DevSecOps Pipeline",
        "features": [
            "Multi-version testing (3.11–3.13)",
            "Shift-left security",
            "Automated CI/CD",
            "Container security",
            "Monitoring ready endpoints"
        ]
    })


# -----------------------------
# RUN
# -----------------------------
if __name__ == '__main__':
    app.run(port=5000)
