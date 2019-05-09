import asyncio
import asyncio_redis

from asyncio_redis.encoders import BytesEncoder

@asyncio.coroutine
def example():
    cursor = yield from protocol.scan(match='*')
    while True:
        item = yield from cursor.fetchone()
        if item is None:
            break
        else:
            print(item)