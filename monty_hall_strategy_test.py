import logging

from monty_hall import logger
from monty_hall.game import Game, Status

logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("log.txt")
logger.addHandler(file_handler)


game_count = 10000
print("Testing 'choose the same door' strategy")
won_games = 0
for i in range(game_count):
    game = Game(door_count=100)
    game.first_guess(1)
    game_won = game.final_guess(1)
    won_games += game_won

print(f"Win rate = {won_games}/{game_count}")


print("Testing 'choose the other door' strategy")
won_games = 0
for i in range(game_count):
    game = Game(door_count=100)
    empty_doors = game.first_guess(1)
    empty_doors.append(1)
    doors = list(range(1, game.door_count + 1))
    final_door = (set(doors) - set(empty_doors)).pop()
    game.final_guess(final_door)
    if game.status == Status.WON:
        won_games += 1
print(f"Win rate = {won_games}/{game_count}")
