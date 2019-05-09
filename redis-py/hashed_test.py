from stand_test import res
if __name__ == '__main__':
    a = {'name': 'json', 'age': '13', 'sex': 'male', 'job': 'coder', 'hobby': 'sleep', }
    res.hmset('hash',a)
    print(res.hget('hash','name'))
    print(res.hget('hash','age'))
    print(res.hget('hash','sex'))
    print(res.hget('hash','job'))
    print(res.hget('hash','hobby'))
    print(res.hgetall('hash'))
    print(res.hmget('hash','name','ismerry'))
    res.hincrby('hash','age','15')
    print(res.hgetall('hash'))