import requests
response = requests.get("https://ipinfo.io/json")
print(response.text)

