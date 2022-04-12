'''

Create an application that interfaces with the user via the CLI - prompt the user with a menu such as:

Please select from the following options (enter the number of the action you'd like to take):
1) Create a new account (POST)
2) View all your tasks (GET)
3) View your completed tasks (GET)
4) View only your incomplete tasks (GET)
5) Create a new task (POST)
6) Update an existing task (PATCH/PUT)
7) Delete a task (DELETE)

It is your responsibility to build out the application to handle all menu options above.


'''

from pprint import pprint
import requests

url = "http://demo.codingnomads.co:8080/tasks_api/users"

#1 & 5 creating new task or account
body = {
    "first_name": "Nayana",
    "last_name": "Das",
    "email": "nayanadas.amrita@gmail.com"
}

response = requests.post(url, json=body)

res = requests.get(url)
data = res.json()
user_json= data["data"]

#2 listing all tasks
for i in range(len(user_json)):
    pprint(user_json[i])


for i in range(len(user_json)):
    if user_json[i]["first_name"]=="Nayana":
        print("Found My information!") #3 similar to listing all completed task
        print(user_json[i])
    else:
        print("Not found!") #4 similar to listing all incompleted task

#6 updating an existing task
body = {
    "first_name": "Marcelia",
    "last_name": "Lashmar",
    "email": "m_lashmar99@uiuc.edu"
}

response = requests.put(url+"/10", json=body)

#7 delete an existing task
response = requests.delete(url+"/140")
