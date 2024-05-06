import requests

url = "https://webook.site/519ba8bf-26cf-b740-0e97ab39869"
payload ={"plato":"pasta","cantidad":1}
response = requests.post(url, data=payload)
print(response.status_code)