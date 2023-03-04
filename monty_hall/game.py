"""
- losuje liczbę 1-3 (wygrywające drzwi)
- input integera (zgadujemy)
- print inne, niewybrane przez nas drzwi, za którymi nic nie ma
"""

import random


def lottery() -> int:
    return random.randint(1, 3)


def first_guess(door: int) -> int:
    lista = [1, 2, 3]
    print(f'Choose number from list: {lista}')
    winning_gate = 1
    lista.remove(door)
    if winning_gate in lista:
        lista.remove(winning_gate)
    revealed_empty_door = random.choice(lista)
    print(f"Zygmunt opens door number {revealed_empty_door} to show there is nothing there!")
    return revealed_empty_door


for i in range(100):
    empty_door = first_guess(1)
