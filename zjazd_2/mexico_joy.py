lista_linijek = open("kod.txt", "r").read().splitlines()
lista_literek = []
for linia in lista_linijek:
    literka = chr(int(linia.replace(" ", "")))
    lista_literek.append(literka)

print("".join(lista_literek))
