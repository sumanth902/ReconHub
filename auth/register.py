from flask import Blueprint, render_template, request, redirect, url_for, flash
import sqlite3
import bcrypt

register_bp = Blueprint("register", __name__)


@register_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        fullname = request.form["fullname"]
        email = request.form["email"]
        password = request.form["password"]

        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt()
        )

        conn = sqlite3.connect("reconhub.db")
        cursor = conn.cursor()

        try:

            cursor.execute(
                """
                INSERT INTO users(fullname,email,password)
                VALUES(?,?,?)
                """,
                (
                    fullname,
                    email,
                    hashed_password.decode("utf-8")
                )
            )

            conn.commit()

            flash("Registration Successful. Please Login.")

            return redirect(url_for("login.login"))

        except sqlite3.IntegrityError:

            flash("Email already exists.")

        finally:

            conn.close()

    return render_template("register.html")