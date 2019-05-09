# coding=UTF-8

import requests
from bs4 import BeautifulSoup
import codecs
import time

DOWNLOAD_URL = 'http://movie.douban.com/top250'


def download_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    return requests.get(url, headers=headers).content


def parse_html(html):
    soup = BeautifulSoup(html, features="html.parser")
    movie_list_soup = soup.find('ol', attrs={'class': 'grid_view'})
    # movie_name_list = []
    movie_name_dict = {}
    for movie_li in movie_list_soup.find_all('li'):
        detail = movie_li.find('div', attrs={'class': 'hd'})
        title = detail.find('span', attrs={'class': 'title'}).getText()
        next_url = detail.find('a')['href']
        movie_name_dict[title] = next_url

    next_page = soup.find('span', attrs={'class': 'next'}).find('a')

    if next_page:
        return movie_name_dict, DOWNLOAD_URL + next_page['href']
    return movie_name_dict, None

def parse_detail_html(html):
    soup = BeautifulSoup(html,features="html.parser")
    info =soup.find('div',attrs={'id':'info'})
    result={}
    director_node = info.find('span')
    director = director_node.find('span', attrs={'class': 'attrs'}).getText()

    editor_node = director_node.find_next_sibling().find_next_sibling()
    editor=editor_node.find('span', attrs={'class':'attrs'}).getText()

    actor_node = info.find('span',{'class':'actor'})#演员层级<span class="actor"><span class="pl">主演</span>: <span class="attrs"><span><a href="/celebrity/1054521/" rel="v:starring">蒂姆·罗宾斯</a> / </span><span><a href="/celebrity/1054534/" rel="v:starring">摩根·弗里曼</a> / </span><span><a href="/celebrity/1041179/" rel="v:starring">鲍勃·冈顿</a> / </span><span><a href="/celebrity/1000095/" rel="v:starring">威廉姆·赛德勒</a> / </span><span><a href="/celebrity/1013817/" rel="v:starring">克兰西·布朗</a> / </span><span style="display: none;"><a href="/celebrity/1010612/" rel="v:starring">吉尔·贝罗斯</a> / </span><span style="display: none;"><a href="/celebrity/1054892/" rel="v:starring">马克·罗斯顿</a> / </span><span style="display: none;"><a href="/celebrity/1027897/" rel="v:starring">詹姆斯·惠特摩</a> / </span><span style="display: none;"><a href="/celebrity/1087302/" rel="v:starring">杰弗里·德曼</a> / </span><span style="display: none;"><a href="/celebrity/1074035/" rel="v:starring">拉里·布兰登伯格</a> / </span><span style="display: none;"><a href="/celebrity/1099030/" rel="v:starring">尼尔·吉恩托利</a> / </span><span style="display: none;"><a href="/celebrity/1343305/" rel="v:starring">布赖恩·利比</a> / </span><span style="display: none;"><a href="/celebrity/1048222/" rel="v:starring">大卫·普罗瓦尔</a> / </span><span style="display: none;"><a href="/celebrity/1343306/" rel="v:starring">约瑟夫·劳格诺</a> / </span><span style="display: none;"><a href="/celebrity/1315528/" rel="v:starring">祖德·塞克利拉</a> / </span><span style="display: none;"><a href="/celebrity/1014040/" rel="v:starring">保罗·麦克兰尼</a> / </span><span style="display: none;"><a href="/celebrity/1390795/" rel="v:starring">芮妮·布莱恩</a> / </span><span style="display: none;"><a href="/celebrity/1083603/" rel="v:starring">阿方索·弗里曼</a> / </span><span style="display: none;"><a href="/celebrity/1330490/" rel="v:starring">V·J·福斯特</a> / </span><span style="display: none;"><a href="/celebrity/1000635/" rel="v:starring">弗兰克·梅德拉诺</a> / </span><span style="display: none;"><a href="/celebrity/1390797/" rel="v:starring">马克·迈尔斯</a> / </span><span style="display: none;"><a href="/celebrity/1150160/" rel="v:starring">尼尔·萨默斯</a> / </span><span style="display: none;"><a href="/celebrity/1048233/" rel="v:starring">耐德·巴拉米</a> / </span><span style="display: none;"><a href="/celebrity/1000721/" rel="v:starring">布赖恩·戴拉特</a> / </span><span style="display: none;"><a href="/celebrity/1333685/" rel="v:starring">唐·麦克马纳斯</a></span><a href="javascript:;" class="more-actor" title="更多主演">更多...</a></span></span>
    #actoress_node=actor_node.find('span', attrs={'class': 'attrs'})#各种演员
    actorname_node = actor_node.find('span')#文本'主演'
    actor1_node = actorname_node.find_next_sibling().find('span')
    actor1_node_node = actor1_node.find_next_sibling().find('span')
    actor1_node_node_node = actor1_node_node.find('a',attrs={'rel':'v:starrign'}).getText()

    actor1 = actor1_node.find('a',{'rel':'v:starring'}).getText()
    actor2 = actor2_node.find('a',{'rel':'v:starring'}).getText()


    result['director']=(director)
    result['editor']=(editor)
    #result['actor']=(actor1,actor2)
    return result

    # content > div.grid-16-8.clearfix > div.article > div.indent.clearfix > div.subjectwrap.clearfix > div.subject.clearfix
    # for movie_detail in soup.find_all('span',attrs={'class':'attrs'}):
    #     movie_d=dict



# if __name__ == '__main__':
#     url = DOWNLOAD_URL
#
#     with codecs.open('movies.txt', 'wb', encoding='utf-8') as fp:
#         while url:
#             html = download_page(url)
#             #movies, url = parse_html(html)
#             #fp.write(movies='\n')
#             #fp.write('\n'.join('{} \n {}'.format(key, value) for key, value in movies.items()))
#             fp.write('\n'.join(parse_detail_html()))
#             time.sleep(1)
if __name__ == '__main__':
    html= download_page('https://movie.douban.com/subject/1292052/')
    p=parse_detail_html(html)
    print(p)
    #with open('movie.txt','wb',encoding='utf-8') as fp:
        #fp.write('\n'.join())