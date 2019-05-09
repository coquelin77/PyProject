from confluent_kafka import Producer
import  json
p = Producer({'bootstrap.servers': 'localhost:9092'})

def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))
def produce_user_info(userinfo):
    p.poll(0)
    #p.produce('first', userinfo.pid.encode('utf-8'), callback=delivery_report)
    p.produce('mul', (json.dumps(userinfo, default=lambda obj: obj.__dict__)), callback=delivery_report)
    p.flush()
if __name__ == '__main__':
    some_data_source=['break','last','python']
    for data in some_data_source:
        print(data)
        # Trigger any available delivery report callbacks from previous produce() calls
        p.poll(0)
        # Asynchronously produce a message, the delivery report callback
        # will be triggered from poll() above, or flush() below, when the message has
        # been successfully delivered or failed permanently.
        p.produce('first', data.encode('utf-8'), callback=delivery_report)

    # Wait for any outstanding messages to be delivered and delivery report
    # callbacks to be triggered.
    p.flush()