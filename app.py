from flask import Flask, render_template, request, send_from_directory
from dotenv import load_dotenv
from core.engine import start_recon
from database import init_db
from services.get_history import get_history
from auth.register import register_bp
from auth.login import login_bp
import os

load_dotenv()

app = Flask(__name__)

# Secret key loaded from .env
app.secret_key = os.getenv("SECRET_KEY")

# -----------------------------
# Authentication
# -----------------------------

app.register_blueprint(register_bp)
app.register_blueprint(login_bp)


# -----------------------------
# Home Page
# -----------------------------

@app.route("/", methods=["GET", "POST"])
def home():

    results = None

    if request.method == "POST":

        target = request.form["target"]

        results = start_recon(target)

        print(results)

    return render_template(
        "index.html",
        results=results
    )


# -----------------------------
# Open PDF / JSON Reports
# -----------------------------

@app.route("/reports/<path:filename>")
def reports(filename):

    reports_folder = os.path.join(
        app.root_path,
        "reports"
    )

    return send_from_directory(
        reports_folder,
        filename,
        as_attachment=False
    )


# -----------------------------
# Scan History
# -----------------------------

@app.route("/history")
def history():

    scans = get_history()

    return render_template(
        "history.html",
        scans=scans
    )


# -----------------------------
# Start Flask
# -----------------------------

if __name__ == "__main__":

    init_db()

    app.run(debug=True)