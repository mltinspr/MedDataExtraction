import requests
from lxml import etree

TARGET_URL = ''


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
    }
    url_response = requests.get(url, headers=headers).text
    return url_response


def parse_html(url_response):
    return etree.HTML(url_response)


def get_data(html):
    pass


if __name__ == '__main__':
    response = get_html(TARGET_URL)
    html = parse_html(response)
