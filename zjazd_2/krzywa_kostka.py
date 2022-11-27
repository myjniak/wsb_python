import random


ciezka_liczba = random.randrange(1, 7)
# print(ciezka_liczba)


def rzut_krzywa_kostka() -> int:
    los = random.randrange(0, 7)
    if los == 0:
        return ciezka_liczba
    return los


