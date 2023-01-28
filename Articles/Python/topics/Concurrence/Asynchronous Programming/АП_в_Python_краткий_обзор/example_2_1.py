import time


def fib(n):
    global count
    count = count + 1
    time.sleep(0.1)
    if n > 1:
        return fib(n - 1) + fib(n - 2)
    return n


start = time.time()
global count
count = 0
result = fib(10)
print(result, count)
print(time.time() - start)
