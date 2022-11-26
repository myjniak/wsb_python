import random

suma = 0
ilosc_prob = 1000000
for j in range(ilosc_prob):
    for i in range(3):
        wynik = random.randrange(1, 7)
        if wynik == 6:
            suma += 1
            break
print(suma)
print('prawdopodobienstwo wynosi :', suma / ilosc_prob * 100, "%")
