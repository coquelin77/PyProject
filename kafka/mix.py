import time, threading
from confluent_kafka import Consumer, KafkaError

# 新线程执行的代码:
def worker(config,topic):
    c = Consumer(config)

    c.subscribe(topic)

    while True:
        msg = c.poll(1.0)

        if msg is None:
            continue
        if msg.error():
            print("Consumer error: {}".format(msg.error()))
            continue

        print(threading.current_thread().name,'Received message: {}'.format(msg.value().decode('utf-8')))
        # write = 'Received message: {}'.format(msg.value().decode('utf-8')+"\n")

    c.close()

if __name__ == '__main__':
    config = {
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'mygroup',
        'auto.offset.reset': 'earliest'
    }
    topic = ['mul']
    t1 = threading.Thread(target=worker, name='ThreadA', args=(config,topic))
    t1.start()
    t2 = threading.Thread(target=worker, name='ThreadB', args=(config,topic))
    t2.start()
    t3 = threading.Thread(target=worker, name='ThreadC', args=(config,topic))
    t3.start()
    print('thread %s ended.' % threading.current_thread().name)