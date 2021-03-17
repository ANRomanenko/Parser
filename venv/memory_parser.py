import requests
from bs4 import BeautifulSoup
import csv

# Пишем константы(Констранта єто та же переменная только в верхнем регистре)

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

# # Пишем проверку для requests
#
# html = get_html(URL)
# print(html)

# Пишем функцию BeautifulSoup

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='product-thumb')
    cards = []
#     print(items)
#
# html = get_html(URL)
# get_content(html.text)

    for item in items:
        cards.append(
            {
                'title':item.find('div', class_='product-name').get_text(strip=True),
                'link':item.find('div', class_='product-name').find('a').get('href')
            }
        )
    return cards

# # Пишем проверку для BeautifulSoup
#
# html = get_html(URL)
# print(get_content(html.text))

# Пишем функцию parser

# def parser():
#     PAGENATION = input('Введите число страниц для парсинга: ')
#     PAGENATION = int(PAGENATION.strip())
#     html = get_html(URL)
#     if html.status_code == 200:
#         cards = []
#         for page in range(1,PAGENATION):
#             print(f'Выполнен парсинг страницы: {page}')
#             html = get_html(URL, params={'page': page})
#             cards.extend(get_content(html.text))
#         print('Спарсено', len(cards), 'карточек товара!')
#     else:
#         'Error'
# parser()

def parser():
    PAGINATION = input('Ввведите число для парсинга страницы: ')
    PAGINATION = int(PAGINATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        cards = []
        for page in range(1, PAGINATION):
            print(f'Выполнен парсинг страницы {page}')
            html = get_html(URL, params={'page': page})
            cards.extend(get_content(html.text))
        print('Спарсено', len(cards), 'карточек товара!')
    else:
        print('Error')
parser()