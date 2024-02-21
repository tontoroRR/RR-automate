import asyncio
import time


class Hoge:
    async def loop(self):
        asyncio.sleep(0.5)
        print("async")
        yield 1

    def __init__(self):
        pass


h, l, ts = Hoge(), asyncio.get_event_loop(), []
for i in range(10):
    ts.append(h.loop())
tasks = asyncio.wait(ts)
