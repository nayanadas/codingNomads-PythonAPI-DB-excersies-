'''
Write a program that makes a PUT request to update your user information to a new first_name, last_name and email.

Again make a GET request to confirm that your information has been updated.

'''
import requests

url = "http://demo.codingnomads.co:8080/tasks_api/users"

body = {
    "first_name": "Nayanaa",
    "last_name": "Dasss",
    "email": "nayanadas@gmail.com"
}

response = requests.put(url+"/164", json=body)

res = requests.get(url)
data = res.json()
user_json= data["data"]

for i in range(len(user_json)):
    if user_json[i]["first_name"]=="Nayanaa":
        print("Found My information!")
        print(user_json[i])
    else:
        print("Not found!")