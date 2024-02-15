import requests

ASANA_API_KEY = "(?i)\\b(?<secret>[0-9]\\/[0-9]{16,}:[a-z0-9]{32,})\\b"

url = 'https://api.asana.com/auth'

headers = {
    'Authorization': f'Bearer {ASANA_API_KEY}',
    'Content-Type': 'application/json'  # Example content type, adjust as needed
}

response = requests.get(url, headers=headers)
