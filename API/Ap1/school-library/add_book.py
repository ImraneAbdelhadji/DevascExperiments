import requests

BASE_URL = "http://library.demo.local/api/v1"
LOGIN_URL = f"{BASE_URL}/loginViaJSON"
BOOKS_URL = f"{BASE_URL}/books"


def get_auth_token():
    r = requests.post(LOGIN_URL, json={
        "username": "cisco",
        "password": "Cisco123!"
    })
    r.raise_for_status()
    token = r.json()["token"]
    print(f"[Token] {token}")
    return token


def add_book(api_key: str):
    payload = {
        "id": 0,
        "title": "DevNet Student Guide",
        "author": "Cisco Student"
    }

    headers = {
        "X-API-Key": api_key,
        "Content-Type": "application/json"
    }

    r = requests.post(BOOKS_URL, headers=headers, json=payload)
    print(f"[POST /books] Status: {r.status_code}")
    print(r.text)


if __name__ == "__main__":
    add_book(get_auth_token())
