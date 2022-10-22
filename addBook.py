import requests
import json


APIHOST = "http://library.demo.local"
LOGIN = "cisco"
PASSWORD = "Cisco123!"

def getAuthToken():
    authCreds = (LOGIN, PASSWORD)
    r = requests.post(
        f"{APIHOST}/api/v1/loginViaBasic", 
        auth = authCreds
    )
    if r.status_code == 200:
        return r.json()["token"]
    else:
        raise Exception(f"Status code {r.status_code} and text {r.text}, while trying to Auth.")

def addBook(book, apiKey):
    r = requests.post(
        f"{APIHOST}/api/v1/books", 
        headers = {
            "Content-type": "application/json",
            "X-API-Key": apiKey
            },
        data = json.dumps(book)
    )
    if r.status_code == 200:
        print(f"Book {book} added.")
    else:
        raise Exception(f"Error code {r.status_code} and text {r.text}, while trying to add book {book}.")

apiKey = getAuthToken()

mid = input ('Masukkan idnya: ')
mnama = input ('Masukkan title bukunya: ')
mauthor = input ('Masukkan author bukunya: ')
misbn = input ('Masukkan isbn bukunya: ')

mid1 = int(mid)

book = {"id":mid1, "title": mnama, "author": mauthor, "isbn": misbn}
addBook(book, apiKey)
