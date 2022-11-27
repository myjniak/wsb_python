slownik = {
    "x": {
        "a": 1, "b": 2, "c": 3
    },
    "y": {
        "a": 4, "b": 5, "c": 6
    },
    "z": {
        "a": 7, "b": 8, "c": 9
    }
}


target = {}
for podslownik in slownik.values():
    for klucz, wartosc in podslownik.items():
        target.setdefault(klucz, []).append(wartosc)


# print(target)

print(list(slownik.values()))
print(list(slownik.keys()))
print(list(slownik.items()))
