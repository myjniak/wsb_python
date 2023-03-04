import logging
from monty_hall import logger
from monty_hall.game import Game
import sys

handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

game = Game()
guess = int(input("Guess a door: "))
game.first_guess(guess)
final_guess = int(input("Guess a door: "))
game.final_guess(final_guess)
