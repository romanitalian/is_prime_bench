import math
from time import perf_counter


def is_prime(num):
    if num == 2:
        return True
    if num == 1 or not num % 2:
        return False
    for div in range(3, int(math.sqrt(num)) + 1, 2):
        if not num % div:
            return False
    return True


def do(n):
    for i in range(n):
        if is_prime(i):
            # print(i)
            pass


if __name__ == '__main__':
    # N = 20
    N = 10_000_000  # 58 sec

    st = perf_counter()
    do(N)
    end = perf_counter()
    print(end - st)
