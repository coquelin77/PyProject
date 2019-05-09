import asyncio
import asyncio_redis

code = \
"""
local value = redis.call('GET', KEYS[1])
value = tonumber(value)
return value * ARGV[1]
"""

@asyncio.coroutine
def example():
    connection = yield from asyncio_redis.Connection.create(host='localhost', port=6379)

    # Set a key
    yield from connection.set('my_key', '2')

    # Register script
    multiply = yield from connection.register_script(code)

    # Run script
    script_reply = yield from multiply.run(keys=['my_key'], args=['5'])
    result = yield from script_reply.return_value()
    print(result) # prints 2 * 5

    # When finished, close the connection.
    connection.close()