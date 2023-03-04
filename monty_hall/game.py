"""
- losuje liczbę 1-3 (wygrywające drzwi)
- input integera (zgadujemy)
- logger.info inne, niewybrane przez nas drzwi, za którymi nic nie ma
"""

import random
from . import logger


class MontyHallBadDoorError(ValueError):
    """When the chosen door number does not exist or are already opened"""


class Game:

    def __init__(self, door_count=3):
        self.door_count = door_count
        self.__winning_door = random.randint(1, door_count)
        self._doors_for_final_guess = []
        self._status = "Not started"

    def first_guess(self, door: int) -> list[int]:
        doors = list(range(1, self.door_count + 1))
        if door not in doors:
            raise MontyHallBadDoorError(f"Door number {door} does not exist. Existing doors: {doors}")
        logger.debug(f"Doors to choose from: {doors}")
        doors.remove(door)
        if door == self.__winning_door:
            remaining_door = random.choice(doors)
            doors.remove(remaining_door)
            self._doors_for_final_guess = [door, remaining_door]
        else:
            doors.remove(self.__winning_door)
            self._doors_for_final_guess = [door, self.__winning_door]
        logger.info(f"Zygmunt opens doors with following numbers: {doors} to show there is nothing there!")
        self._status = "First guess done"
        return doors

    def final_guess(self, door: int) -> bool:
        if door not in self._doors_for_final_guess:
            raise MontyHallBadDoorError(f"Door {door} doesn't exist or is already open.\n"
                                        f"Doors to choose from were: {self._doors_for_final_guess}")
        if door == self.__winning_door:
            logger.info("YOU WON")
            self._status = "Won"
            return True
        else:
            logger.info("YOU LOST")
            self._status = "Lost"
            return False

