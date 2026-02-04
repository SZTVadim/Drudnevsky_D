import requests


# """POST - запрос"""

data_for_post = {
    "id": 7878,
    "category": {"id": 7878, "name": "СОБАКИ"},
    "name": "doggie",
    "photoUrls": ["string"],
    "tags": [{"id": 1, "name": "ЭЛЛИ"}],
    "status": "available",
}

headers_for_post = {"accept": "application/json", "Content-Type": "application/json"}

url_post = "https://petstore.swagger.io/v2/pet"

response_post = requests.post(url_post, json=data_for_post, headers=headers_for_post)

print(f" Обьект создан  Status cod : {response_post.status_code}")
print(f" Тело ответа POST: {response_post.json()}")

# """GET - запрос"""


headers_for_get = {
    "accept": "application/json",
}

response_get = requests.get(
    "https://petstore.swagger.io/v2/pet/7878", headers=headers_for_get
)

print(f" Status Code, GET - запроса {response_get.status_code}")
print(f" Тело , GET - запроса {response_get.json()}")


# """PUT - запрос"""

data_for_put = {
    "id": 7878,
    "category": {"id": 7878, "name": "СОБАКИ"},
    "name": "Джек",
    "photoUrls": ["string"],
    "tags": [{"id": 1, "name": "Элли-Скай-Вай"}],
    "status": "available",
}

headers_for_put = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

url_put = "https://petstore.swagger.io/v2/pet"

response_put = requests.put(url_post, json=data_for_put, headers=headers_for_put)

print(f"Status code  PUT  : {response_put.status_code}")
print(f"Тело ответа PUT  : {response_put.json()}")

# """Delete"""

url_delete = "https://petstore.swagger.io/v2/pet/7878"
headers_delete = {"accept": "application/json"}

response_delete = requests.delete(url_delete, headers=headers_delete)

print(f"Status code  Delete : {response_delete.status_code}")
print(f"Тело ответа  Delete: {response_delete.json()}")
