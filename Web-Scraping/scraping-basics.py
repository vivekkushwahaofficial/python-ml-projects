import requests
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com'
responce = requests.get(url)

soup = BeautifulSoup(responce.text, 'html5lib')

for item in soup.find_all('tr', class_='athing'):
  title_span = item.find('span', class_='titleline')

  if title_span:
    link = title_span.find('a')
    
    if link:
        print(link.text)