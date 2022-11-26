kurs_euro = 4.67


def get_salary_in_pln(string):
    zarobki, waluta = string.split()
    waluta = waluta.upper()
    if waluta == "EUR":
        zarobki_w_zl = kurs_euro * float(zarobki)
    elif waluta == "PLN":
        zarobki_w_zl = float(zarobki)
    else:
        raise ValueError(f"Nie obsluguje waluty {waluta}")
    return zarobki_w_zl


zarobki = {}
while True:
    pracownik = input("Imie i nazwisko pracownika: ")
    kwota = input("Ile zarabia? ")
    if pracownik == "" and kwota == "":
        break
    zarobki_w_zl = get_salary_in_pln(kwota)
    zarobki[pracownik] = zarobki_w_zl

for pracownik, zarobki_w_pln in zarobki.items():
    print(f"Pracownik {pracownik} zarabia {zarobki_w_pln}PLN")
