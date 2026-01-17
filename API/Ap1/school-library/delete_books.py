import requests

API_HOST = "http://library.demo.local/api/v1/books/{}"

def getAuthToken():
    r = requests.post("http://library.demo.local/api/v1/loginViaJSON",
                      json={"username":"cisco","password":"Cisco123!"})
    return r.json()["token"]

def deleteBook(book_id, apiKey):
    r = requests.delete(API_HOST.format(book_id),
                        headers={
                            "Content-type":"application/json",
                            "X-API-Key": apiKey
                        })
    if r.status_code == 200:
        print(f"Book {book_id} deleted")
    else:
        raise Exception(f"Error code {r.status_code}")

apiKey = getAuthToken()

for i in range(190,200):
    deleteBook(i, apiKey)
