from produce import *
import redis

class News(object):
    def __init__(self,id,title,content,author):
        self.id=id
        self.title=title
        self.comtent=content
        self.author=author



#while True:
def view():
    res = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

    fresh_news_list = res.lrange('news:top:100',0,9)
    result = []
    for id in fresh_news_list:
        #print(res.hgetall('news:' + str(id)))
        news_map = res.hgetall('news:' + str(id))
        title = news_map['title']
        content = news_map['content']
        author = news_map['author']
        news_item = News(id,title,content,author)
        result.append(news_item)
    return result
if __name__ == '__main__':
    result = view()
    print(result)
    for news in result:
        print('id:' + news.id + ', title:' + news.title + ', contect:' + news.comtent + ', author:' + news.author)