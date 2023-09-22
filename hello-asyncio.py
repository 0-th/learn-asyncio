"""
Simple example to demo core asyncio functionality
"""

import asyncio
import time


# Coroutine
async def async_greet():
    """Coroutine that sleeps for a random amount of time"""
    print("Hello")
    await asyncio.sleep(1)
    print("Bye")


async def main():
    await asyncio.gather(async_greet(), async_greet(), async_greet())


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print(f"Runtime of the program {__file__} is {(end - start):0.2f}secs")
