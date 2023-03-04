"""
- losuje liczbę 1-3 (wygrywające drzwi)
- input integera (zgadujemy)
- print inne, niewybrane przez nas drzwi, za którymi nic nie ma
"""

import random


class Game:

    def __init__(self, door_count=3):
        self.door_count = door_count
        self.__winning_door = random.randint(1, door_count)

    def first_guess(self, door: int) -> int:
        doors = list(range(1, self.door_count + 1))
        doors.remove(door)
        if self.__winning_door in doors:
            doors.remove(self.__winning_door)
        revealed_empty_door = random.choice(doors)
        print(f"Zygmunt opens door number {revealed_empty_door} to show there is nothing there!")
        return revealed_empty_door

    def final_guess(self, door: int) -> bool:
        if door == self.__winning_door:
            print("YOU WON")
            return True
        else:
            print("YOU LOST")
            return False
