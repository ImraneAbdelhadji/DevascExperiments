import requests

BASE_URL = "http://library.demo.local/api/v1"
LOGIN_URL = f"{BASE_URL}/loginViaJSON"
BOOKS_URL = f"{BASE_URL}/books"


def get_auth_token():
    r = requests.post(LOGIN_URL, json={"username": "cisco", "password": "Cisco123!"})
    r.raise_for_status()
    token = r.json()["token"]
    print(f"[Token] {token}")
    return token


def get_books(api_key: str):
    r = requests.get(BOOKS_URL, headers={"X-API-Key": api_key})
    print(f"[GET /books] Status: {r.status_code}")
    print(r.text)


if __name__ == "__main__":
    key = get_auth_token()
    get_books(key)
