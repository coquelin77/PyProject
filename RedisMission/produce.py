import redis
import time
#when I wrote this codes,God and I knew what it mean
#Now only God just know
res = redis.Redis(host='localhost', port=6379, db=0,decode_responses=True)

if __name__ == '__main__':

    res.delete('news')
    res.delete('hash')
    for i in range(0,500):
        res.lpush('news',i)
        hash = {'id':str(i),'title':'title'+str(i),'content':'content'+str(i),'author':'author'+str(i)}
        #res.hmset('hash',)
        res.ltrim('news',0,9)
        res.hmset('hash'+str(i),hash)
        time.sleep(.5)
        print(res.lrange('news',0,-1))
        print(res.hgetall('hash'+str(i)))
        h=res.lrange('news',0,-1)
        g=res.hgetall('hash'+str(i))
