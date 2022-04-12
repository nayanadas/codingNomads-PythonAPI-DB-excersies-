'''
Write a program that makes a DELETE request to remove the user your create in a previous example.

Again, make a GET request to confirm that information has been deleted.

'''
import requests

url = "http://demo.codingnomads.co:8080/tasks_api/users"

response = requests.delete(url+"/164")

res = requests.get(url)
data = res.json()
user_json= data["data"]

for i in range(len(user_json)):
    if user_json[i]["first_name"]=="Nayanaa":
        print("Found My information!")
    else:
        print("Not found!")