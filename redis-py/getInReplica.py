import redis
import time
res = redis.Redis(host='localhost', port=6380, db=0,decode_responses=True)

if __name__ == '__main__':
    print(res.get('test'))