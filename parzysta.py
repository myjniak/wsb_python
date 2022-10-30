import time

liczba = input("Podaj liczbę: ")

if int(liczba) % 2:
    time.sleep(2)
    print("nieparzysta")

else:
    time.sleep(4)
    print("liczba parzysta")
