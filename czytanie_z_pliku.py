with open("czytanie_z_pliku.txt", "r", encoding="UTF-8") as plik:
    print(plik.read())
"""Context manager:"""
# ekwiwalent:
plik = open("czytanie_z_pliku.txt", "r", encoding="UTF-8")
print(plik.read())
plik.close()


print("plik jest zamkniety")