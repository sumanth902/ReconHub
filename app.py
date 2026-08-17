from flask import (
    Flask,
    render_template,
    request,
    send_from_directory,
    session,
    redirect,
    url_for
)

from dotenv import load_dotenv

from core.engine import start_recon
from database import init_db
from services.get_history import get_history

from auth.register import register_bp
from auth.login import login_bp
from auth.logout import logout_bp

import os


# =============================
# Load Environment Variables
# =============================

load_dotenv()


# =============================
# Flask Application
# =============================

app = Flask(__name__)


# Secret key from .env
app.secret_key = os.getenv("SECRET_KEY")


# =============================
# Authentication
# =============================

app.register_blueprint(register_bp)
app.register_blueprint(login_bp)
app.register_blueprint(logout_bp)


# =============================
# Home / Main Dashboard
# =============================

@app.route("/", methods=["GET", "POST"])
def home():

    # Login protection
    if "user_id" not in session:
        return redirect(url_for("login.login"))

    results = None

    if request.method == "POST":

        target = request.form["target"]

        results = start_recon(target, session["user_id"])

        print(results)

    return render_template(
        "index.html",
        results=results
    )


# =============================
# PDF / JSON Reports
# =============================

@app.route("/reports/<path:filename>")
def reports(filename):

    # Login protection
    if "user_id" not in session:
        return redirect(url_for("login.login"))

    reports_folder = os.path.join(
        app.root_path,
        "reports"
    )

    return send_from_directory(
        reports_folder,
        filename,
        as_attachment=False
    )


# =============================
# Scan History
# =============================

@app.route("/history")
def history():

    # Login protection
    if "user_id" not in session:
        return redirect(url_for("login.login"))

    scans = scans = get_history(session["user_id"])

    return render_template(
        "history.html",
        scans=scans
    )


# =============================
# GitHub
# =============================

@app.route("/github")
def github_page():

    # Login protection
    if "user_id" not in session:
        return redirect(url_for("login.login"))

    return redirect(
        "https://github.com/sumanth902/ReconHub"
    )


# =============================
# Documentation
# =============================

@app.route("/documentation")
def documentation_page():

    if "user_id" not in session:
        return redirect(url_for("login.login"))

    return render_template("documentation.html")


# =============================
# Start Flask
# =============================

if __name__ == "__main__":

    init_db()

    debug_mode = os.getenv("FLASK_DEBUG", "False").lower() == "true"

    app.run(debug=debug_mode)
