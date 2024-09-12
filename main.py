import requests
from bs4 import BeautifulSoup


url = 'https://www.adrenaline.com.br/noticias/'                    
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')

article = parsed_html.find('div', class_='archive-list-posts')

noticias = article.find_all('h2')

x=1
print('Notícias do Dia:')

for notica in noticias:
    print(f'{x}', notica.text)
    x += 1
