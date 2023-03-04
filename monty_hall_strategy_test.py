from monty_hall.game import Game


print("Testing 'choose the same door' strategy")
won_games = 0
for i in range(1000):
    game = Game()
    game.first_guess(1)
    game_won = game.final_guess(1)
    won_games += game_won

print(f"Win rate = {won_games}/1000")


print("Testing 'choose the other door' strategy")
won_games = 0
for i in range(1000):
    # ...???