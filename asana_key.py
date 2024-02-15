import requests

ASANA_API_KEY = 'qkt6zxj8bph!DCT!vat'

url = 'https://api.asana.com/auth'

headers = {
    'Authorization': f'Bearer {ASANA_API_KEY}',
    'Content-Type': 'application/json'  # Example content type, adjust as needed
}

response = requests.get(url, headers=headers)
