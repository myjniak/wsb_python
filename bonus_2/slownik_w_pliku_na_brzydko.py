slownik = {
    "c": 1,
    "b": 2
}
slownik["a"] = 3
print(slownik)



plik = open("slownik.txt", "w")
plik.write(str(slownik))
plik.close()

plik = open("slownik.txt", "r")
slownik = plik.read()

slownik = slownik.replace("{", "").replace("}", "")
pociachany = slownik.split(", ")

zrekonstruowany_slownik = {}
for para in pociachany:
    klucz = para.split("'")[1]
    wartosc = para.split(":")[-1].strip()
    zrekonstruowany_slownik[klucz] = int(wartosc)
print(zrekonstruowany_slownik)
