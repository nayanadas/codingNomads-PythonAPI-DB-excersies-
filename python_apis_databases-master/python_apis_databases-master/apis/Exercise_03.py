'''
Write the necessary code to make a POST request to:

    http://demo.codingnomads.co:8080/tasks_api/users

and create a user with your information.

Make a GET request to confirm that your user information has been saved.

'''

import requests

url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "first_name": "Nayana",
    "last_name": "Das",
    "email": "nayanadas.amrita@gmail.com"
}

response = requests.post(url, json=body)

res = requests.get(url)
data = res.json()
user_json= data["data"]

for i in range(len(user_json)):
    if user_json[i]["first_name"]=="Nayana":
        print("Found My information!")
        print(user_json[i])
    else:
        print("Not found!")