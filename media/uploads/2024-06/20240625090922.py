import requests

url = 'http://firstproject-667917fda8a2f.mockapi.uz'

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}

# Student GET
response = requests.get(url + '/Student', headers=headers)
print(response.json())

# Student POST
data = {
    'name': 'person.firstName',
    'phone_number': 'phoneNumber.phoneNumber',
}

response = requests.post(url + '/Student', headers=headers, json=data)
print(response.json())

# Student PUT
data = {
    'name': 'person.firstName',
    'phone_number': 'phoneNumber.phoneNumber',
}
response = requests.put(url + '/Student/:id', headers=headers, json=data)
print(response.json())

# Student DELETE
response = requests.delete(url + '/Student/:id', headers=headers)
print(response.json())

# Group GET
response = requests.get(url + '/Student/:id/Group', headers=headers)
print(response.json())

# Group POST
data = {
    'name': 'person.firstName',
}
response = requests.post(url + '/Student/:id/Group', headers=headers, json=data)
print(response.json())

# Group PUT
data = {
    'name': 'person.firstName',
}
response = requests.put(url + '/Student/:id/Group/:id', headers=headers, json=data)
print(response.json())

# Group DELETE
response = requests.delete(url + '/Student/:id/Group/:id', headers=headers)
print(response.json())

