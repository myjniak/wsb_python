class MontyHallInvalidStatusError(Exception):
    """When action is invalid because of state of the game"""


class MontyHallBadDoorError(ValueError):
    """When the chosen door number does not exist or are already opened"""
