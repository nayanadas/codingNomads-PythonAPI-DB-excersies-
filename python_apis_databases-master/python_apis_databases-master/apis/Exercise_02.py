'''
Building on the previous example, create a list of all of the emails of the users and print
the list to the console.

'''
import requests
from pprint import pprint

url = "http://demo.codingnomads.co:8080/tasks_api/users"
response = requests.get(url)
data = response.json()
user_json= data["data"]
email_list=[]

for i in range(len(user_json)):
    email_list.append(user_json[i]["email"])

print(email_list)
