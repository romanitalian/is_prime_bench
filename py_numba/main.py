import math
from time import perf_counter

from numba import njit


@njit(fastmath=True)
def is_prime(num):
    if num == 2:
        return True
    if num == 1 or not num % 2:
        return False
    for div in range(3, int(math.sqrt(num)) + 1, 2):
        if not num % div:
            return False
    return True


@njit(fastmath=True)
def do(n):
    for i in range(n):
        is_prime(i)


# python3 ./py_numba/main.py
# 3.829456385
if __name__ == '__main__':
    # N = 20
    N = 10_000_000  # 58 sec
    st = perf_counter()
    do(N)
    end = perf_counter()
    print(end - st)
