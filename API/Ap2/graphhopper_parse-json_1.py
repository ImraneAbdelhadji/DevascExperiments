import requests, urllib.parse

geocode_url = "https://graphhopper.com/api/1/geocode?"
route_url   = "https://graphhopper.com/api/1/route?"
loc1 = "Rome, Italy"
loc2 = "Baltimore, Maryland"
key  = "4513fc24-8369-452a-bd27-b290fb52bead"

url = geocode_url + urllib.parse.urlencode({"q": loc1, "limit": "1", "key": key})
reply = requests.get(url)
json_data = reply.json()
print(json_data)           # tijdelijke check