import json

linijki_pliku = open("wyniki_f1.txt").read().splitlines()
ranking = {}
for linia in linijki_pliku:
    zawodnik, punktacja = linia.split(",")
    ranking[zawodnik] = int(punktacja)

print(json.dumps(ranking, indent=4))

print(sorted(ranking))
