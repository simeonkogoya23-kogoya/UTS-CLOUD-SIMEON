import aiohttp
import asyncio
import time

URL = "https://jsonplaceholder.typicode.com/todos/1"

async def fetch_json(session):
    async with session.get(URL) as response:
        return await response.json()

async def main():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_json(session) for _ in range(10)]
        results = await asyncio.gather(*tasks)
    end = time.time()

    print("ASYNCIO RESULTS:", results)
    print("TIME:", end - start)

if __name__ == "__main__":
    asyncio.run(main())
