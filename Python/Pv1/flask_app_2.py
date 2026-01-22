from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", datetime_time=datetime.datetime.now())

@app.route("/time")
def time():
    return render_template("time.html")

@app.route("/map")
def map():
    return render_template("map.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

    return render_template("login.html")

@app.route("/account")
def account():
    return render_template("account.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8802)
