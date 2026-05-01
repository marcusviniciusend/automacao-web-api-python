import requests

BASE_URL = "https://petstore.swagger.io/v2"

HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}


def get(endpoint, params=None):
    return requests.get(f"{BASE_URL}{endpoint}", headers=HEADERS, params=params)


def post(endpoint, body):
    return requests.post(f"{BASE_URL}{endpoint}", headers=HEADERS, json=body)


def put(endpoint, body):
    return requests.put(f"{BASE_URL}{endpoint}", headers=HEADERS, json=body)


def delete(endpoint):
    return requests.delete(f"{BASE_URL}{endpoint}", headers=HEADERS)


def post_form(endpoint, data):
    return requests.post(f"{BASE_URL}{endpoint}", data=data)


def post_file(endpoint, file_bytes, filename="test.jpg"):
    files = {"file": (filename, file_bytes, "image/jpeg")}
    return requests.post(f"{BASE_URL}{endpoint}", files=files)
