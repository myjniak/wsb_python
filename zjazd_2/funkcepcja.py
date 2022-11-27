def wynonaj_n_razy(funkcja, n, x):
    for i in range(n):
        x = funkcja(x)
    return x


def razy_3_plus_1(n):
    return n * 3 + 1


def wykonaj_n_razy_3n_plus_1(n, x):
    def razy_3_plus_1(n):
        return n * 3 + 1
    for i in range(n):
        x = razy_3_plus_1(x)
    return x

# for i in range(4):
#     x = razy_3_plus_1(x)
x = wynonaj_n_razy(razy_3_plus_1, 4, 3)
print(x)
x = wykonaj_n_razy_3n_plus_1(4, 3)
print(x)
