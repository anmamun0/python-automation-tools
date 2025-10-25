import time
from functools import lru_cache 


@lru_cache(maxsize=4)
def some_work(n):

    time.sleep(n)
    return n

if __name__ == '__main__':
    print('How running some work')
    print(some_work(3))

    print('2 running some work')
    print(some_work(3))

    print('3 running some work')
    print(some_work(3))

    print('4 running some work')
    print(some_work(3))
    print('All Done')


