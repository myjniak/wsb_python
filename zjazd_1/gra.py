"""
Gra w "zgadnij jaką liczbę mam na myśli" :)
Program przyjmuje liczbę od gracza, po czym podpowiada "więcej" lub "mniej" aż gracz odgadnie.

Potrzebujemy: while, input, if, print
"""

import random

zagadka = True
liczba = random.randrange(1, 100)

while zagadka:
    a = int(input("Podaj liczbę: "))

    if a > liczba:
        print("liczba jest mniejsza")
    elif a < liczba:
        print("liczba jest większa")
    else:
        print("poprawna liczba")
        zagadka = False
