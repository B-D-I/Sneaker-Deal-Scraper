from bs4 import BeautifulSoup
import requests
from datetime import datetime

today = str(datetime.now().date())


def get_name_from_url(url):
    site_url_name = url.split('w.'[1])
    site_url_name = site_url_name[1]
    return site_url_name


def deal_scraper(url, item_list_name):
    site_url = url
    site_name = get_name_from_url(site_url)
    page = requests.get(site_url)
    content = page.content
    soup = BeautifulSoup(content, "html.parser")
    title = soup.title.text

    items = soup.findAll('div', {'class': f'{item_list_name}'})
    with open(f"{site_name}.txt", "w", newline="") as f:
        f.write(today)
        f.write('\n')
        f.write(title)
        f.write('\n')
        for item in items:
            urls = item.find('img')
            src = urls.get('src')
            if site_name == 'sneakerdealsgb':
                description = item.find('pre').text.strip()
                description = str(description.encode('utf-8')).replace(r"\xc2\xa3", "£")
            elif site_name == 'sneakersnstuff':
                brand = item.find('span', class_='card__brand')
                name = item.find('strong', class_='card__name')
                price_before = item.find('del', class_='price__original')
                price_after = item.find('span', class_='price__current')
                description = brand, ' ', name, '\n', price_before, '\n', price_after

            image_url = f'\nIMAGE URL:\n{src}'
            full_description = f'\nDESCRIPTION\n{description}'

            f.write(image_url)
            f.write('\n')
            f.write(full_description)
            f.write('\n--------------------------------------\n')


deal_scraper('https://www.sneakerdealsgb.com/sneaker-deals/', 'grid-item-content')
deal_scraper('https://www.sneakersnstuff.com/en-gb/56/sale', 'product-list')
