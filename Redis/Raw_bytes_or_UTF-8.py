import asyncio
import asyncio_redis

from asyncio_redis.encoders import BytesEncoder

@asyncio.coroutine
def example():
    # Create Redis connection
    connection = yield from asyncio_redis.Connection.create(host='localhost', port=6379, encoder=BytesEncoder())

    # Set a key
    yield from connection.set(b'my_key', b'my_value')

    # When finished, close the connection.
    connection.close()