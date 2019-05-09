import asyncio
import asyncio_redis

@asyncio.coroutine
def example():
    loop = asyncio.get_event_loop()

    # Create Redis connection
    transport, protocol = yield from loop.create_connection(
                asyncio_redis.RedisProtocol, 'localhost', 6379)

    # Set a key
    yield from protocol.set('my_key', 'my_value')

    # Get a key
    result = yield from protocol.get('my_key')
    print(result)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(example())