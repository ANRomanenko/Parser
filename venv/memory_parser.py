import requests
from bs4 import BeautifulSoup
import csv

CSV = 'cards.csv'
HOST = 'https://talvi-ukraine.com/'
URL = 'https://talvi-ukraine.com/shapki/kupit-dlya_malchikov/'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}

# Пишем функцию requests

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

# Пишем функцию BeautifulSoup

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='product-thumb')
    cards = []

    for item in items:
        cards.append(
            {
                'title':item.find('div', class_='product-name').get_text(strip=True)
            }
        )
    return cards

# Пишем функцию parser

def parser():
    html = get_html(URL)
    if html.status_code == 200:
        pass
    else:
        print('Error')

parser()