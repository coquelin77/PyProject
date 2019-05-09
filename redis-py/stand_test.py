import redis
import time
res = redis.Redis(host='localhost', port=6379, db=0,decode_responses=True)
#print(res.get('incredible').decode("utf-8"))




if __name__ == '__main__':
    #set
    res.set('foo', 'bar')
    print(res.get('foo'))
    #mset
    a = {'key1': 'v1', 'key2': 'v2', 'key3': 'v3', 'key4': 'v4', 'key5': 'v5', 'key6': 'v6', }
    res.mset(a)
    print(res.get('key1')+res.get('key2')+res.get('key3')+res.get('key4')+res.get('key5')+res.get('key6'))
    #mget
    print(res.mget('key1','key2','key3','key4','key5','key6',))
    #INCR
    res.set('incredible','12')
    res.incr('incredible','10')
    print(res.get('incredible'))
    res.incr('incredible')
    print(res.get('incredible'))
    text=res.get('incredible')
    #exists
    print(res.exists('key1'))
    if(res.exists('key1')==1):
        print('存在')
    elif(res.exists('key1')==0):
        print('不存在')
    print(res.exists('key'))
    print(res.exists('incredible'))
    print(res.exists('incr'))
    #delete
    res.delete('key')
    if (res.exists('key') == 1):
        print('存在')
    elif (res.exists('key') == 0):
        print('不存在')
    #type
    res.set('flew','3.14')
    print(res.type('flew'))
    res.delete('flew')
    print(res.type('flew'))
    #expire
    res.set('timer','nolonger')
    res.expire('timer','5')
    print(res.get('timer'))
    time.sleep(3)
    print(res.get('timer'))
    time.sleep(1)
    print(res.get('timer'))
    time.sleep(1)
    print(res.get('timer'))
    #set ex and ttl
    res.set('ttl','i m alive',ex=10)
    print('I will be terminated in'+str(res.ttl('ttl'))+'sec')
    time.sleep(1)
    print('I will be terminated in' +str(res.ttl('ttl')) + 'sec')
    time.sleep(1)
    print('I will be terminated in' + str(res.ttl('ttl')) + 'sec')
    time.sleep(1)
    print('I will be terminated in' +str(res.ttl('ttl'))+ 'sec')
    time.sleep(1)
    print('I will be terminated in' + str(res.ttl('ttl')) + 'sec')
    time.sleep(1)
    print('I will be terminated in' +str(res.ttl('ttl')) + 'sec')
    time.sleep(1)
    print('I will be terminated in' + str(res.pttl('ttl')) + 'psec')
    time.sleep(1)
    print('I will be terminated in' + str(res.ttl('ttl')) + 'sec')
    time.sleep(1)
    print('I will be terminated in' +str(res.ttl('ttl')) + 'sec')
    time.sleep(1)
    print('I will be terminated in' + str(res.ttl('ttl')) + 'sec')
    time.sleep(1)
    print('I will be terminated in' +str(res.ttl('ttl')) + 'sec')
    if(res.ttl('ttl')==-1):
        print('I am always alive')
    elif(res.ttl('ttl')==-2):
        print("I don't exist anymore")
    else:
        print('I will be terminated in' + str(res.ttl('ttl')) + 'sec')