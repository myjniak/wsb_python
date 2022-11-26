"""
input: 3
jeśli liczba jest nieparzysta:  n*3+1
jeśli liczba jest parzysta: n/2

powtarzaj algorytm dopóki nie osiąniesz 1

3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

"""


def collatz_step(x: int) -> int:
    if x % 2 == 0:
        wynik = x // 2
    else:
        wynik = x * 3 + 1
    return wynik


def collatz_convergence(n: int):
    if n <= 1:
        print("Liczba musi być większa od 1")
    wynik = [n]
    while n > 1:
        n = collatz_step(n)
        wynik.append(n)
    return wynik


# 1 - 500
list = []
for i in range(2, 500):
    x = len(collatz_convergence(i))
    list.append(x)
print(list.index(max(list)) + 2)



rekord = 0
rekordowa_ilosc_iteracji = 0
for i in range(2, 500):
    ilosc_iteracji = len(collatz_convergence(i))
    if ilosc_iteracji > rekordowa_ilosc_iteracji:
        rekordowa_ilosc_iteracji = ilosc_iteracji
        rekord = i

print("Liczba", rekord)
print("Osiagnela rekordowa ilosc iteracji: ", rekordowa_ilosc_iteracji)
