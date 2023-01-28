import asyncio, time


async def fib(n):
    global count
    count = count + 1
    time.sleep(0.1)
    event_loop = asyncio.get_event_loop()
    if n > 1:
        task1 = asyncio.create_task(fib(n - 1))
        task2 = asyncio.create_task(fib(n - 2))
        await asyncio.gather(task1, task2)
        return task1.result() + task2.result()
    return n


start = time.time()
global count
count = 0
result = asyncio.run(fib(10))
print(result, count)
print(time.time() - start)
