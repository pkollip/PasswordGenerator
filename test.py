import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes":10, "name": "Tim", "views": 10},
        {"likes":1000, "name": "Elon", "views": 100000},
        {"likes":1000000, "name": "Praval", "views": 1000000000}]
for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())


input()
response = requests.get(BASE + "video/2")
print(response.json())