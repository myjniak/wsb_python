import datetime
import json


ludzie: list[dict[str, any]] = [
    {
        "imie": "Kasia",
        "PESEL": "98110929882",
        "data urodzenia": "09.11.1998"
    },
    {
        "imie": "Paweł",
        "PESEL": "95021429882",
        "data urodzenia": "14.02.1996"
    },
    {
        "imie": "Alicja",
        "PESEL": "90011029882",
        "data urodzenia": "10.01.1990"
    }
]
zdrobnienia = {
    "Paweł": "Pawełek",
    "Alicja": "Ala",
    "Kasia": "Kasieńka"
}


for czlowiek in ludzie:
    imie = czlowiek["imie"]
    zdrobnione_imie = zdrobnienia[imie]
    czlowiek["imie"] = zdrobnione_imie

print(ludzie)


for czlowiek in ludzie:
    if czlowiek["PESEL"][:2] == czlowiek["data urodzenia"][-2:]:
        print("Jest ok.")
    else:
        print(f'{czlowiek["imie"]} ma nieprawidłowe dane.')


#  Dopisz do kazdej osoby z listy ludzie klucz "rok urodzenia"
for czlowiek in ludzie:
    data_urodzenia = czlowiek["data urodzenia"]
    rok = data_urodzenia[-4:]
    czlowiek["rok urodzenia"] = rok


# Dopisz do kazdej osoby z listy klucz "plec" - (jeśli imie kończy się na "a")
for czlowiek in ludzie:
    if czlowiek["imie"].endswith("a"):
        czlowiek['plec'] = 'K'
    else:
        czlowiek['plec'] = 'M'


# Dopisz do każdej osoby z listy klucz "wiek"
# wiek (w przybliżeniu) to aktualny rok minus data ur.
aktualny_rok = datetime.date.today().year
for czlowiek in ludzie:
    wiek = aktualny_rok - int(czlowiek["rok urodzenia"])
    czlowiek["wiek"] = wiek


print(json.dumps(ludzie, indent=4))

#  1: W grupie ludzi X% to mężczyźni.
ilosc_wszystkich = len(ludzie)
ilosc_mezczyzn = 0
for czlowiek in ludzie:
    if czlowiek["plec"] == "M":
        ilosc_mezczyzn += 1
procent_mezczyzn = ilosc_mezczyzn/ilosc_wszystkich * 100
print(f"W grupie mamy {procent_mezczyzn:.2f}% mezczyzn")


#  2: Wszyscy ludzie w grupie są pełnoletni. / nie
wszyscy_sa_pelnoletni = True
for czlowiek in ludzie:
    if czlowiek["wiek"] < 18:
        wszyscy_sa_pelnoletni = False

# alternatywa
wszyscy_sa_pelnoletni = all(map(lambda czlowiek: czlowiek["wiek"] >= 18, ludzie))
if wszyscy_sa_pelnoletni:
    print("Wszyscy sa pelnoletni")
else:
    print("Nie wszyscy sa pelnoletni!")
