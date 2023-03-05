from monty_hall.game import Game


def gotowanie_pierogow():
    print("przyrzadzam ciasto")
    print("wałkuję i lepię")
    print("wrzucam do wrzątku")
    print("wyciągam")
    moje_pierogi = 50
    game = Game()
    game.first_guess(1)
    game.pierogi = moje_pierogi
    return game


costam = gotowanie_pierogow()
print(f"ugotowalem {costam.pierogi} pierogów :D")

