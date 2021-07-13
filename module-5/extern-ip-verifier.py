import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

answer = urlopen(url)

data = json.load(answer)

ip = data['ip']
org = data['org']
city = data['city']
country = data['country']
region = data['region']

print(f'''Detalhes do IP externo\n\

IP: {ip}\n\
Região: {region}\n\
País: {country}\n\
Cidade: {city}\n\
Org: {org}''')