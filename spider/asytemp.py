#python2
import trollius
from trollius import From

@asyncio.coroutine
def function(,,):
    pass

loop = asyncio.get_event_loop()

tasks =[
        asyncio.async(function(,,)),
        
        ]

loop.run_until_complete(asyncio.wait(tasks))

loop.close()

#python3
import asyncio
@asyncio.coroutine
def function(name, number):
    pass

loop = asyncio.get_event_loop()

tasks = [
        asyncio.async(function(,,)),

        ]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
