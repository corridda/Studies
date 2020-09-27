import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def refined(s):
    # 1,470 total ratings
    r = s.split(' ')[0]   # 1,470
    return r.replace(',', '') # 1470


def write_csv(data):
    with open('plugins.tsv', 'a', newline='') as f:
        writer = csv.writer(f, delimiter='\t')

        writer.writerow(
            (
                data['name'],
                data['url'],
                data['reviews'],
            )
        )


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    popular = soup.find('div', id='page').find('div', id='content').find('main', id='main').find_all('section')[3]
    plugins = popular.find_all('article') # 4

    with open('plugins.tsv', 'w', newline='') as f:
        csv.DictWriter(f, ['name', 'url', 'reviews'], delimiter='\t').writeheader()

    for plugin in plugins:
        # [ plugin1, plugin2, plugin3, plugin4 ]
        name = plugin.find('h3').text
        url = plugin.find('h3').find('a').get('href')

        r = plugin.find('span', class_='rating-count').find('a').text
        rating = refined(r)

        data = {'name': name,
                'url': url,
                'reviews': rating }

        # print(data)
        write_csv(data)



def main():
    url = 'https://wordpress.org/plugins/'
    get_data(get_html(url))



if __name__ == '__main__':
    main()
