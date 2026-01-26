# Fill in this file with the rooms/spaces listing code from the Webex Teams exercise
import requests

access_token = 'MmVlYzRmZWUtNGM5Zi00NDJkLTgzZGItOTNkY2ZmYzQzOWM0MTQxOGE2YWUtNzNi_P0A1_14a2639d-5e4d-48b4-9757-f4b8a23372de'
url = 'https://webexapis.com/v1/rooms'

headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}

params = {'max': '100'}
res = requests.get(url, headers=headers, params=params)
print(res.json())
