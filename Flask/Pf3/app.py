from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "765c26843c0ca5230864251a31dcbdb7"

@app.route("/", methods=["GET", "POST"])
def home():
    weather = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")

        if city:
            url = (
                "https://api.openweathermap.org/data/2.5/weather"
                f"?q={city}&appid={API_KEY}&units=metric"
            )

            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                weather = {
                    "city": city,
                    "temp": data["main"]["temp"],
                    "desc": data["weather"][0]["description"]
                }
            else:
                error = "Stad niet gevonden"

    return render_template("index.html", weather=weather, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
