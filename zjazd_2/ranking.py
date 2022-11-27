import json

linijki_pliku = open("wyniki_f1.txt").read().splitlines()
ranking = {}
for linia in linijki_pliku:
    zawodnik, punktacja = linia.split(",")
    ranking[zawodnik] = int(punktacja)

# print(json.dumps(ranking, indent=4))

def get_2nd_element(x):
    return x[1]


s = sorted(ranking.items(), key=get_2nd_element, reverse=True)

print(f"Wygrywa {s[0][0]} z {s[0][1]}pkt")
print(f"2 miejsce: {s[1][0]} z {s[1][1]}pkt")
print(f"3 miejsce: {s[2][0]} z {s[2][1]}pkt")
