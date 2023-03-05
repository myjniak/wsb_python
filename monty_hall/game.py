"""
- losuje liczbę 1-3 (wygrywające drzwi)
- input integera (zgadujemy)
- logger.info inne, niewybrane przez nas drzwi, za którymi nic nie ma
"""

import random


from . import logger
from .game_status import Status
from .exceptions import MontyHallInvalidStatusError, MontyHallBadDoorError


class Game:

    __slots__ = ["door_count", "__winning_door", "_doors_for_final_guess", "_status"]

    def __init__(self, door_count=3):
        self.door_count = door_count
        self.__winning_door = random.randint(1, door_count)
        self._doors_for_final_guess = []
        self._status: Status = Status.NOT_STARTED

    @property
    def status(self):
        return self._status

    def first_guess(self, door: int) -> list[int]:
        if self._status != Status.NOT_STARTED:
            raise MontyHallInvalidStatusError("Status for first guess has to be 'NOT STARTED'.\n"
                                              f"Actual state: {self._status}")
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
        self._status = Status.FIRST_GUESS
        return doors

    def final_guess(self, door: int) -> bool:
        if self._status != Status.FIRST_GUESS:
            raise MontyHallInvalidStatusError("Status for final guess has to be 'FIRST_GUESS'.\n"
                                              f"Actual state: {self._status}")
        if door not in self._doors_for_final_guess:
            raise MontyHallBadDoorError(f"Door {door} doesn't exist or is already open.\n"
                                        f"Doors to choose from were: {self._doors_for_final_guess}")
        if door == self.__winning_door:
            logger.info("YOU WON")
            self._status = Status.WON
            return True
        else:
            logger.info("YOU LOST")
            self._status = Status.LOST
            return False


if __name__ == "__main__":
    import pdb
    game = Game()
    pdb.set_trace()
