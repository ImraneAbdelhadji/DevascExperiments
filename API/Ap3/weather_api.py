import requests

api_key = "765c26843c0ca5230864251a31dcbdb7" #Als je een nieuwe api maakt het pakt een beetje tijd voor dat het werkt 

while True:
    city = input("Geef een stad in (of q om te stoppen): ")

    if city == "q" or city == "quit":
        break

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        "?q=" + city +
        "&appid=" + api_key +
        "&units=metric"
    )

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temperature = data["main"]["temp"]
        description = data["weather"][0]["description"]

        print("===================================")
        print("Stad:", city)
        print("Temperatuur:", temperature, "°C")
        print("Weer:", description)
        print("===================================")
    else:
        print("Foutcode:", response.status_code)
        print("API antwoord:", data)

