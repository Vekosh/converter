import requests
import json
url = "https://api.apilayer.com/fixer/convert?to=GBP&from=EUR&amount=5"

payload = {}
headers= {
  "apikey": "eBvUBFsWXaNAtUx6Uhtsr985Z0baHWZi"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
print(result)

# {
#   "date": "2018-02-22",
#   "historical": "",
#   "info": {
#     "rate": 148.972231,
#     "timestamp": 1519328414
#   },
#   "query": {
#     "amount": 25,
#     "from": "GBP",
#     "to": "JPY"
#   },
#   "result": 3724.305775,
#   "success": true
# }