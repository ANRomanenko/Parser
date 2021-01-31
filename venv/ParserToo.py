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

def get_html(url, params=''):
    r = requests.get(url, headers = HEADERS, params = params)
    return r

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='product-thumb')
    cards = []

    for item in items:
        cards.append(
            {
                'code': item.find('div', class_='product-code').get_text(strip=True),
                'title':item.find('div', class_='product-name').get_text(strip=True),
                'link_product': item.find('div', class_='product-name').find('a').get('href'),
                'price': item.find('span', class_='price-new').get_text(strip=True),
                'image_card': item.find('div', class_='category-product-image').find('img').get('src')
            }
        )
    return cards

def save_doc(items, path):
    with open(path, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(["Артикул", 'Имя', 'Ссылка на шапку', 'Базовая цена', 'Изображения'])
        for item in items:
            writer.writerow([item['code'], item['title'], item['link_product'], item['price'], item['image_card']])

def parser():
    PAGINATION = input('Укажите количество страниц для парсинка: ')
    PAGINATION = int(PAGINATION.strip())
    html = get_html(URL)
    if html.status_code == 200:
        cards = []
        for page in range(1, PAGINATION):
            print(f'Парсинг страницы: {page}')
            html = get_html(URL, params={'page' : page})
            cards.extend(get_content(html.text))
            save_doc(cards,CSV)
        print('Парсинг завершён!!!')
    else:
        print('Error')

parser()