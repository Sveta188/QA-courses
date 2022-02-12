import requests


def get_request():
    response_1 = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Authors")
    print("List of authors: ", response_1.text)
    print(response_1.url)
    response_2 = requests.get("https://fakerestapi.azurewebsites.net/api/v1/Authors/12")
    print(response_2.text)
    print(response_2.url)


def post_request():
    response_1 = requests.post("https://fakerestapi.azurewebsites.net/api/v1/Books", json={
        "id": 3456,
        "title": "NewPOSt",
        "description": "fghjkl",
        "pageCount": 765,
        "excerpt": "fghj",
        "publishDate": "2022-01-02T17:20:51.352Z"
    })
    print(response_1.text)

    response_2 = requests.post("https://fakerestapi.azurewebsites.net//api/v1/Users", json={
        "id": 11,
        "userName": "Sveta",
        "password": "rtyuiop"
    })
    print(response_2.text)


def put_request():
    r = requests.put("https://fakerestapi.azurewebsites.net/api/v1/Books/10", data={"title": "Book 12"})
    print(r.status_code)


def delete_request():
    delt = requests.delete("https://fakerestapi.azurewebsites.net//api/v1/Users/4")
    print(delt.status_code)


print(get_request())
print()
print(post_request())
print()
print(put_request())
print()
print(delete_request())