from bs4 import BeautifulSoup
import requests
import string

site = requests.get('https://www.climatempo.com.br/').content
soup = BeautifulSoup(site, 'html.parser')

print(soup.title)
