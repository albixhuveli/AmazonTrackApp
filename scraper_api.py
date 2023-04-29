import json
import requests

API_KEY = '<YOUR-API-KEY-HERE>'
SCRAPER_URL = 'https://ecom.webscrapingapi.com/v1'

PARAMS = {
    "api_key":API_KEY,
    "engine":"amazon",
    "type":"product",
    "product_id":"B09FQ35SW6"
}

response = requests.get(SCRAPER_URL, params=PARAMS)

parsed_result = json.loads(response.text)
title = parsed_result['product_results']['title']
price = parsed_result['product_results']['price']


print(title)
print(price)