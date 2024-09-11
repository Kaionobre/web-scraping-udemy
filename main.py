import requests
from bs4 import BeautifulSoup

url = 'https://noticias.uol.com.br/'

response = requests.get(url)

html = response.text
html_convertido = BeautifulSoup(html, 'html.parser')

print(html_convertido.title)