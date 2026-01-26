import requests

access_token = 'MmVlYzRmZWUtNGM5Zi00NDJkLTgzZGItOTNkY2ZmYzQzOWM0MTQxOGE2YWUtNzNi_P0A1_14a2639d-5e4d-48b4-9757-f4b8a23372de'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vODBjM2Q0YTAtZmFhOS0xMWYwLWI2ZDItZWY2N2Y4ZTlmOGE4'
message = 'Hello **DevNet Associates**!!'

url = 'https://webexapis.com/v1/messages'

headers = {
    'Authorization': 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
}

params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())
