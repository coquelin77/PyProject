from stand_test import res
if __name__ == '__main__':
    res.sadd('set','1','2','3')
    res.sadd('set','4')
    print(res.smembers('set'))
    print(res.sismember('set', 3))
    print(res.sismember('set',5))

    res.sadd('add','administrator')
    print(res.smembers('add'))
    print(res.sinter('set','add'))#交集
    print(res.sunion('set','add'))#并集
