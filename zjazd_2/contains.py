lista = [1, 2, 3]

slownik = {
    "c": 1,
    "b": 2
}
slownik["a"] = 3


for _ in slownik.items():
    print(_)
