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

def deleteBook(apiToken):
    r = requests.delete(
        f"{APIHOST}/api/v1/books/0", 
        headers = {
            "Content-type": "application/json",
            "X-API-Key": apiKey
        },
    )
    if r.status_code == 200:
        return r.json()
    else:
        raise Exception(f"Error code {r.status_code} and text {r.text}, while trying to add book {book}.")

apiKey = getAuthToken()
#print(apiKey)

apiDelete = deleteBook(apiKey)