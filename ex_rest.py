import requests
import json

user = {
    "id" : "gildong",
    "password" : "1q2w3e4r",
    "age" : 30
}

json_data = json.dumps(user, indent = 4)
print(json_data)

with open("user.json", "w", encoding = "utf-8") as file:
    json.dump(user, file, indent = 4)

target = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url = target)

data = response.json()

name_list = []
for x in data:
    name_list.append(x['name'])

print(name_list)