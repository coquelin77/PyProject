from  stand_test import res
if __name__ == '__main__':
    res.sadd('desk','草花1','草花2','草花3','草花4','草花5','草花6','草花7','草花8','草花9','草花10','草花J','草花Q','草花K','方片1','方片2','方片3','方片4','方片5','方片6','方片7','方片8','方片9','方片10','方片J','方片Q','方片K','红桃1','红桃2','红桃3','红桃4','红桃5','红桃6','红桃7','红桃8','红桃9','红桃10','红桃J','红桃Q','红桃K','黑桃1','黑桃2','黑桃3','黑桃4','黑桃5','黑桃6','黑桃7','黑桃8','黑桃9','黑桃10','黑桃J','黑桃Q','黑桃K')
    print(res.smembers('desk'))
    res.sunionstore('round1','desk')
    print(res.smembers('round1'))
    print(res.spop('round1'))
    print(res.spop('round1'))
    print(res.spop('round1'))
    print(res.spop('round1'))
    print(res.spop('round1'))
    print(res.scard('round1'))