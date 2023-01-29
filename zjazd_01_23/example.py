import json
from more_itertools import first


with open("wyniki.json") as plik:
    slownik = json.load(plik)


# max = 0
# name = ""
# for j in slownik['drivers']:
#     if j['points'] > max:
#         max = j['points']
#         name = j['name']
# print(f"Wygrał: {name} punkty: {max}")


drivers = sorted(slownik["drivers"], key=lambda driver: driver["points"], reverse=True)

name = first(drivers)["name"]
points = first(drivers)["points"]
print(f"{name} wygral z {points} punktami")
