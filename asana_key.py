import requests

ASANA_API_KEY = "1/1234567890123456:abcdefghijklmnopqrstuvwx1"

url = 'https://api.asana.com/auth'

headers = {
    'Authorization': Authorization {ASANA_API_KEY}',
    'Content-Type': 'application/json'  # Example content type, adjust as needed
}

response = requests.get(url, headers=headers)
