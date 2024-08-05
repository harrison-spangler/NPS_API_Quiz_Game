import requests

api_key = 'OBqnBdbJmLHP3KsDag2TEVcK2eCXhv41VbgwU6Ae'
url = 'https://developer.nps.gov/api/v1/parks'
params = {'api_key': api_key}

response = requests.get(url, params=params)
parks_json = response.json()
print(parks_json)