from bs4 import BeautifulSoup
import requests
from datetime import datetime


def sneaker_deals():
    site_url = 'https://www.sneakerdealsgb.com/sneaker-deals/'
    site_name = get_name_from_url(site_url)
    page = requests.get(site_url)
    content = page.content
    soup = BeautifulSoup(content, "html.parser")
    today = str(datetime.now().date())
    title = soup.title.text

    items = soup.findAll('div', {'class': 'grid-item-content'})
    with open(f"{site_name}.txt", "w", newline="") as f:
        for item in items:
            urls = item.find('img')
            src = urls.get('src')
            description = item.find('pre').text.strip()
            description = str(description.encode('utf-8')).replace(r"\xc2\xa3", "£")
            image_url = f'\nIMAGE URL:\n{src}'
            full_description = f'\nDESCRIPTION\n{description}'

            f.write(today)
            f.write('\n')
            f.write(title)
            f.write('\n')
            f.write(image_url)
            f.write('\n')
            f.write(full_description)


def sneakers_n_stuff():
    site_url = 'https://www.sneakersnstuff.com/en-gb/56/sale'
    site_name = get_name_from_url(site_url)
    page = requests.get(site_url)
    content = page.content
    soup = BeautifulSoup(content, "html.parser")
    today = str(datetime.now().date())
    title = soup.title.text
    items = soup.findAll('div', {'class': 'product-list'})

    with open(f"{site_name}.txt", "w", newline="") as f:
        for item in items:
            urls = item.find('img')
            src = urls.get('src')
            brand = item.find('span', class_='card__brand')
            name = item.find('strong', class_='card__name')
            description = brand, ' ', name
            price_before = item.find('del', class_='price__original')
            price_after = item.find('span', class_='price__current')

            image_url = f'\nIMAGE URL:\n{src}'
            full_description = f'\nDESCRIPTION\n{description}\n{price_before}\n{price_after}'

            f.write(today)
            f.write('\n')
            f.write(title)
            f.write('\n')
            f.write(image_url)
            f.write('\n')
            f.write(full_description)


def get_name_from_url(url):
    site_url_name = url.split('w.'[1])
    site_url_name = site_url_name[1]
    return site_url_name


sneakers_n_stuff()