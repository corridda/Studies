#! usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import csv
import re
from urllib.parse import urljoin


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('cmc.csv', 'a', newline='') as f:
        writer = csv.writer(f)

        writer.writerow(
            (
                data['name'],
                data['url'],
                data['price']
            )
        )


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    trs = None
    for t in soup.find_all('table'):
        if (body := t.find('tbody')) is not None:
            if len(trs := body.find_all('tr')) >= 100:
                break
        else:
            continue

    with open('cmc.csv', 'w', newline='') as f:
        csv.DictWriter(f, ['name', 'url', 'price']).writeheader()

    for tr in trs:
        tds = tr.find_all('td')
        try:
            name = tds[1].find('a', class_='cmc-link').text
            url = urljoin('https://coinmarketcap.com/', tds[1].find('a').get('href'))
            price = tds[3].find('a').text
            price = re.sub('["$, ]', repl='', string=price)

            data = {'name': name,
                    'url': url,
                    'price': price}

            write_csv(data)
        except IndexError:
            pass



def main():
    url = 'https://coinmarketcap.com/'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
