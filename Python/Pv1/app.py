from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = "devasc_secret_key"
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

    username = request.form["username"]
    password = request.form["password"]
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

    username = request.form["username"]
    password = request.form["password"]
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
        session["user"] = username
        return redirect(url_for("map"))

    return "Foute login"

# -------------------------
# MAP (AFGESCHERMD)
# -------------------------
@app.route("/map")
def map():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("map.html", user=session["user"])

# -------------------------
# LOGOUT
# -------------------------
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/time")
def map():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("time.html", user=session["user"])

# -------------------------
# MAIN
# -------------------------
if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5555)
