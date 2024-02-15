import requests

ASANA_API_KEY = "Authorization: Bearer ACCESS_TOKEN"

url = 'https://api.asana.com/auth'

headers = {
    'Authorization': {ASANA_API_KEY}',
    'Content-Type': 'application/json'  # Example content type, adjust as needed
}

response = requests.get(url, headers=headers)
