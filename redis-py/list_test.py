from stand_test import res
#list.l/rpush
if __name__ == '__main__':

    res.delete('list')
    alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for j in alphabet:
        res.rpush('list',j)
    print(res.lrange('list',0,-1))
    #list.l/rpop
    #print(res.rpop('list'))
    #print(res.lrange('list',0,-1))
    for i in range (0,len(alphabet)):
        print(res.rpop('list'))
        print(res.lrange('list',0,-1))
        print(res.lpush('list',i))
        print(res.lrange('list', 0, -1))
    res.ltrim('list',0,19)
    print(res.lrange('list',0,-1))
    print(res.brpop('list',5))