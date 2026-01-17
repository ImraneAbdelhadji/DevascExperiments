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


def update_book(book_id: int, api_key: str):
    payload = {
        "title": "check DevNet Student Guide",
        "author": "Cisco Student test",
        "pages": 300
    }

    url = f"{BOOKS_URL}/{book_id}"
    r = requests.put(url, headers={"X-API-Key": api_key}, json=payload)
    print(f"[PUT /books/{book_id}] Status: {r.status_code}")
    print(r.text)


if __name__ == "__main__":
    key = get_auth_token()
    update_book(1, key)   # change ID as needed
