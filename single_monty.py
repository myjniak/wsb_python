from monty_hall.game import Game

game = Game()
guess = int(input("Guess a door: "))
game.first_guess(guess)
final_guess = int(input("Guess a door: "))
game.final_guess(final_guess)
