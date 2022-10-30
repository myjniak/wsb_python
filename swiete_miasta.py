"""Printujemy tylko miasta zaczynające się od "Saint", "Santa" albo "San" """

# Uzywajac tylko narzedzi ktore znamy:
miasta = open("miasta.csv")
for linia in miasta:
    if "," in linia:
        # podziel linie na elementy oddzielajac je przecinkiem i wez przedostatni element
        sekcja_z_miastem = linia.split(",")[-2]
        # zastap znak " niczym (czyli usun znaki ") i usun niepotrzebne spacje (strip())
        miasto = sekcja_z_miastem.replace('"', '').strip()
        if miasto.startswith("Saint ") or miasto.startswith("Santa ") or miasto.startswith("San "):
            print(miasto)
miasta.close()


# Nieco ladniej :)
with open("miasta.csv") as miasta:
    for linia in miasta:
        if not linia.strip():
            continue
        miasto = linia.split(",")[-2].replace('"', '').strip()
        miasto_jest_swiete = (miasto.startswith("Saint ") or
                              miasto.startswith("Santa ") or
                              miasto.startswith("San "))
        if miasto_jest_swiete:
            print(miasto)
