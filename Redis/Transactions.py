import asyncio
import asyncio_redis

@asyncio.coroutine
def example(loop):
    # Create Redis connection
    connection = yield from asyncio_redis.Pool.create(host='localhost', port=6379, poolsize=10)

    # Create transaction
    transaction = yield from connection.multi()

    # Run commands in transaction (they return future objects)
    f1 = yield from transaction.set('key', 'value')
    f2 = yield from transaction.set('another_key', 'another_value')

    # Commit transaction
    yield from transaction.exec()

    # Retrieve results
    result1 = yield from f1
    result2 = yield from f2

    # When finished, close the connection pool.
    connection.close()
