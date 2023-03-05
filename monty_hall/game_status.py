from enum import Enum


class Status(Enum):
    NOT_STARTED = "Not started"
    FIRST_GUESS = "First guess done"
    WON = "Won"
    LOST = "Lost"


if __name__ == "__main__":
    print(Status.WON)
    print(f"type of {Status.WON} value: {type(Status.WON.value)}")
    instance = Status("Lost")
    print(instance)
