import requests
import json

headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer kaIUKPMS2ivA8n4V1iTE99CQUGcG'
}
url = 'https://sandbox.tradier.com/v1/markets/quotes?symbols='

symbol = 'spy'
#symbol = input("Input desired symbol here:").lower()

r = requests.get(url + symbol, headers=headers)

result = json.loads(r.text)
print(json.dumps(result, indent=2, sort_keys=True))

quote = result['quotes']['quote']
