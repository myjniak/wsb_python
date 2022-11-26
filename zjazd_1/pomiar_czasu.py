from time import time


def silnia_i(n: int) -> int:
    wynik = 1
    for i in range(2, n + 1):
        wynik = wynik * i
    return wynik


def silnia_r(n):
    if n > 1:
        return n * silnia_r(n - 1)
    elif n in (0, 1):
        return 1


start = time()
for i in range(10000):
    silnia_i(900)
stop = time()
print(stop - start)


start = time()
for i in range(10000):
    silnia_r(900)
stop = time()
print(stop - start)