from confluent_kafka import Consumer, KafkaError

c = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'mygroup',
    'auto.offset.reset': 'earliest'
})

c.subscribe(['mul'])
file = input('filename')
while True:
    msg = c.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        #print("Consumer error: {}".format(msg.error()))
        continue

    print('Received message: {}'.format(msg.value().decode('utf-8')))
    #write = 'Received message: {}'.format(msg.value().decode('utf-8')+"\n")
'''
    with open('./text'+file+'.txt', 'a') as f:
        f.write(write)
        f.write(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    time.sleep(5)
'''
c.close()