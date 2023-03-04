"""
- losuje liczbę 1-3 (wygrywające drzwi)
- input integera (zgadujemy)
- logger.info inne, niewybrane przez nas drzwi, za którymi nic nie ma
"""

import random
from . import logger


class Game:

    def __init__(self, door_count=3):
        self.door_count = door_count
        self.__winning_door = random.randint(1, door_count)

    def first_guess(self, door: int) -> int:
        doors = list(range(1, self.door_count + 1))
        logger.debug(f"Doors to choose from: {doors}")
        doors.remove(door)
        if self.__winning_door in doors:
            doors.remove(self.__winning_door)
        revealed_empty_door = random.choice(doors)
        logger.info(f"Zygmunt opens door number {revealed_empty_door} to show there is nothing there!")
        return revealed_empty_door

    def final_guess(self, door: int) -> bool:
        if door == self.__winning_door:
            logger.info("YOU WON")
            return True
        else:
            logger.info("YOU LOST")
            return False
