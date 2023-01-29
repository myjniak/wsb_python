class Czlowiek:
    __slots__ = "waga", "wzrost"

    ma_mozg = True
    ilosc_konczyn = 4
    przeciwwstawny_kciuk = True
    gromada = "ssak"

    def __init__(self, waga: float, wzrost: int):
        self.waga = waga
        self.wzrost = wzrost


maciek = Czlowiek(76, 179)
blazej = Czlowiek(66, 199)
Czlowiek.waga = 50
maciek.nazwisko = "Pyton"  # tak nie wolno, bo __slots__ definiuje jedyne dozwolone attrybuty
print(maciek.nazwisko)
print(blazej.waga)
print(maciek.gromada)
print(maciek.waga)
# 1. szukam maciek.waga w atrybutach macka
# 2. szukam maciek.waga w atrybutach Człowiek
