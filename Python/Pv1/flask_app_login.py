from flask import Flask, request, render_template, redirect, url_for, session
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = "devasc-secret-key"   # nodig voor sessions

DB_NAME = "user.db"

# -------------------------
# DATABASE
# -------------------------
def get_db():
    return sqlite3.connect(DB_NAME)

def init_db():
    db = get_db()
    c = db.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password_hash TEXT NOT NULL
        )
    """)
    db.commit()
    db.close()

# -------------------------
# HOME
# -------------------------
@app.route("/")
def home():
    return render_template("index.html")

# -------------------------
# SIGNUP
# -------------------------
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")

    username = request.form.get("username")
    password = request.form.get("password")

    password_hash = hashlib.sha256(password.encode()).hexdigest()

    db = get_db()
    c = db.cursor()
    try:
        c.execute(
            "INSERT INTO users VALUES (?, ?)",
            (username, password_hash)
        )
        db.commit()
        return redirect(url_for("login"))
    except sqlite3.IntegrityError:
        return "Gebruiker bestaat al"
    finally:
        db.close()

# -------------------------
# LOGIN
# -------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    username = request.form.get("username")
    password = request.form.get("password")
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    db = get_db()
    c = db.cursor()
    c.execute(
        "SELECT password_hash FROM users WHERE username = ?",
        (username,)
    )
    record = c.fetchone()
    db.close()

    if record and record[0] == password_hash:
        session["user"] = username   # 👈 login onthouden
        return redirect(url_for("account"))

    return "Foute login"

# -------------------------
# ACCOUNT
# -------------------------
@app.route("/account")
def account():
    if "user" not in session:
        return redirect(url_for("login"))

    return render_template("account.html", user=session["user"])

# -------------------------
# LOGOUT (optioneel maar netjes)
# -------------------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

# -------------------------
# MAIN
# -------------------------
if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5555)
