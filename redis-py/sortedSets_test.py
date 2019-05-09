from stand_test import res
if __name__ == '__main__':
    a = {'Alan Kay': '1940', 'Sophie Wilson': '1957', 'Richard Stallman': '1953', 'Anita Borg': '1949',
         'Yukihiro Matsumoto': '1965', 'Hedy Lamarr': '1914', 'Claude Shannon': '1916', 'Linus Torvalds': '1969',
         'Alan Turing': '1912'}
    b={'jason':1942}
    res.zadd('sort',a)
    print(res.zrange('sort',0,-1,withscores=True))#value写前面，后面是分数