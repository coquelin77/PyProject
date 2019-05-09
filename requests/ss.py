# coding=UTF-8

import requests
from bs4 import BeautifulSoup
import codecs
import time


def download_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    return requests.get(url, headers=headers).content


def parse_detail_html(html):
    soup = BeautifulSoup(html, features="html.parser")
    frame = soup.find('table', attrs={'role': 'grid'})
    ss = frame.find('td')
    result = {}
    print(ss)
    # info = frame.find_all('td')
    # return info


if __name__ == '__main__':
    html = download_page('https://free-ss.site/')
    p = parse_detail_html(html)
    print(p)
    # with open('movie.txt','wb',encoding='utf-8') as fp:
    # fp.write('\n'.join())
