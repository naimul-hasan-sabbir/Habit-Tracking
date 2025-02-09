import requests
from datetime import datetime

USERNAME = "naimul"
TOKEN = "123456789"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPH_ID,
    "name" : "Cycling Graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
#print(today.strftime("%Y%m%d"))

pixel_data = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : input("How many kilometers did you cycle today ? \n"),
}

response = requests.post(url=pixel_creation_endpoint, headers=headers, json=pixel_data)
print(response.json())

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity" : "15.2"
}

# response = requests.put(url=update_endpoint, headers=headers, json=new_pixel_data)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

#response = requests.delete(url=delete_endpoint, headers=headers)