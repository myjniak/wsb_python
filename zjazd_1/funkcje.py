def dodaj_10_do(x: int | float):
    wynik = x + 10
    return wynik


liczba_z_dodana_10 = dodaj_10_do(4.67)
print(liczba_z_dodana_10)


def silnia_i(n: int) -> int:
    wynik = 1
    for i in range(2, n + 1):
        wynik = wynik * i
    return wynik


print(silnia_i(5))


def silnia_r(n):
    if n > 1:
        return n * silnia_r(n - 1)
    elif n in (0, 1):
        return 1


print(silnia_r(5))


def fibonacci(numer) -> int:
    if numer < 0:
        print("Incorrect input")
    elif numer == 0:
        return 0
    elif numer == 1 or numer == 2:
        return 1
    else:
        return fibonacci(numer - 1) + fibonacci(numer - 2)


print(fibonacci(9))


def fibo(x: int):
    if x == 0:
        wynik = 0
    elif x == 1:
        wynik = 1
    else:
        wynik = fibo(x - 2) + fibo(x - 1)
    return wynik


print(fibo(9))
