import requests
from bs4 import BeautifulSoup
import csv

# Пишем константы

CSV = 'cards.csv'
HOST = 'https://talvi-ukraine.com/'
URL = 'https://talvi-ukraine.com/shapki?product_id=4687'
HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36'
}

# Пишем функцию requests

def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

# Пишем функцю BeautifulSoup

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='row')
    cards = []
    for item in items:
        cards.append(
            {
                'list':item.find('div', class_='aboutThisItem__description-content').get_text(strip=True)
            }
        )
    return cards

# Пишем функцию parser

def parser():
    PAGINATION = input('Введите число страниц для пагинации парсинга: ')
    PAGINATION = int(PAGINATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        cards = []
        for page in range(1, PAGINATION):
            print(f'Выполнен парсинг страницы: {page}')
            html = get_html(URL, params={'page': page})
            cards.extend(get_content(html.text))
        print('Парсинг закончен спарсено', len(cards))
    else:
        print('Error')
parser()