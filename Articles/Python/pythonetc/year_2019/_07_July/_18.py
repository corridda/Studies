"""https://t.me/pythonetc/424"""

"""If you want to measure time between two events you should use time.monotonic() instead of time.time().
time.monotonic() never goes backwards even if system clock is updated:"""

from contextlib import contextmanager
import time


@contextmanager
def timeit():
    start = time.monotonic()
    yield
    print(time.monotonic() - start)


if __name__ == '__main__':
    with timeit():
        print('before')
        time.sleep(1)
        print('after')
