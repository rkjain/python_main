import requests
api_url = "http://shibe.online/api/shibes"

params = {
    'count': 10
}

api_response = requests.get(api_url, params=params)

# status code
print(api_response.status_code)

# Response in json

json_resp = api_response.json()


for url in json_resp:
    print(url)
