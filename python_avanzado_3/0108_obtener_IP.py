import requests
import public_ip as ip

request = requests.get("https://ident.me")
ip_publica = request.text
print(ip_publica)
ip_publica_2 = ip.get()
print(ip_publica_2)