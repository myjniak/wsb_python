"""
niemutowalne typy zmiennych:
str
int
float
bool
tuple

mutowalne typy zmiennych:
list
dict
"""



lista = [1, 2, 3, 4, 5, 7]
print(id(lista))
lista[2] = 99
lista.append(235)
print(lista)
print(id(lista))


napis = "pierogi"
# napis[2] = "s" - tak nie możemy zrobić :(
print(id(napis))
napis = "hotd" + napis[-3:]
print(napis)
print(id(napis))
