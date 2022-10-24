import requests
import json
y = input("Выберите одну из 3 валют EUR, USD, GBP: ").strip(" / .")
x = input("Выберите в какую валюту хотите переводить EUR, USD, GBP: ").strip(" / .")
amount = int(input("Введите сумму: "))
url = f"https://api.apilayer.com/fixer/convert?to={x}&from={y}&amount={amount}"

payload = {}
headers= {
  "apikey": "eBvUBFsWXaNAtUx6Uhtsr985Z0baHWZi"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
val_sum = json.loads(result)
# print(val_sum)

print(val_sum["query"], sep=' ', end='\n')
print(f"result = ", (val_sum["result"]))
# vfj