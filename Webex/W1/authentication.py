# Fill in this file with the authentication code from the Webex Teams exercise
import requests
import json

access_token = 'MmVlYzRmZWUtNGM5Zi00NDJkLTgzZGItOTNkY2ZmYzQzOWM0MTQxOGE2YWUtNzNi_P0A1_14a2639d-5e4d-48b4-9757-f4b8a23372de'
url = 'https://webexapis.com/v1/people/me'

headers = {
    'Authorization': 'Bearer {}'.format(access_token)
}

res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
