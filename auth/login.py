from functools import wraps
from flask import session, redirect, url_for
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import sqlite3
import bcrypt

login_bp = Blueprint("login", __name__)


@login_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        conn = sqlite3.connect("reconhub.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, fullname, email, password FROM users WHERE email = ?",
            (email,)
        )

        user = cursor.fetchone()

        conn.close()

        if user:

            stored_password = user[3].encode("utf-8")

            if bcrypt.checkpw(
                password.encode("utf-8"),
                stored_password
            ):

                session["user_id"] = user[0]
                session["fullname"] = user[1]
                session["email"] = user[2]

                flash("Login successful.")

                return redirect(url_for("home"))

        flash("Invalid email or password.")

    return render_template("login.html")