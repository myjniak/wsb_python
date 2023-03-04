import logging

from monty_hall import logger
from monty_hall.game import Game

logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("log.txt")
logger.addHandler(file_handler)


game_count = 1000
print("Testing 'choose the same door' strategy")
won_games = 0
for i in range(game_count):
    game = Game()
    game.first_guess(1)
    game_won = game.final_guess(1)
    won_games += game_won

print(f"Win rate = {won_games}/{game_count}")


print("Testing 'choose the other door' strategy")
won_games = 0
for i in range(game_count):
    game = Game()
    empty_doors = game.first_guess(1)
    doors = list(range(1, game.door_count + 1))
    doors.remove(1)
    # doors.remove(empty_door)  usuń empty_doors z doors ????
    game_won = game.final_guess(doors[0])
    won_games += game_won
print(f"Win rate = {won_games}/{game_count}")
