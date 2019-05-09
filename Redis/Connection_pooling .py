import asyncio
import asyncio_redis

@asyncio.coroutine
def example():
    # Create Redis connection
    connection = yield from asyncio_redis.Pool.create(host='localhost', port=6379, poolsize=10)

    # Set a key
    yield from connection.set('my_key', 'my_value')

    # When finished, close the connection pool.
    connection.close()