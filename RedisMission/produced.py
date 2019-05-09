import redis
import time
res = redis.Redis(host='localhost', port=6379, db=0,decode_responses=True)

if __name__ == '__main__':

    res.delete('news:top:100')
    i = 0
    while True:

        #在列表插入一条新闻，从左端加入
        res.lpush('news:top:100',i)
        #只保留列表中前100条新闻
        res.ltrim('news:top:100',0,99)

        #为当前这条新闻生成对应的hash表
        news = {'id':str(i), 'title':'title' + str(i), 'content':'content' + str(i), 'author':'author' + str(i)}
        res.hmset('news:' + str(i), news)

        print(res.lrange('news:top:100', 0, -1))
        print(res.hgetall('news:' + str(i)))

        i = i + 1
        time.sleep(1)