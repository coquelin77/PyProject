from confluent_kafka import Producer
import time
from ff import userinfo
import  producer

for i in range(0,500):


    b = i+1
    a = "user"
    both = "%s%d" % (a, b)
    print(both)
    #time.sleep(1)
    user = userinfo(both,i)

    producer.produce_user_info(user)

