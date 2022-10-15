"""Obliczmy średnią długość słowa z tekstu 'dlugi_tekst'"""

dlugi_tekst = """Lorem Ipsum is simply dummy text of the printing and typesetting industry.
 Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
 when an unknown printer took a galley of type and scrambled it to make a type specimen book.
  It has survived not only five centuries, but also the leap into electronic typesetting,
   remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset
    sheets containing Lorem Ipsum passages, and more recently with desktop publishing software
     like Aldus PageMaker including versions of Lorem Ipsum."""

lista_slow = dlugi_tekst.split()
ilosc_liter = 0
for slowo in lista_slow:
    ilosc_liter += len(slowo)
print(ilosc_liter/len(lista_slow))
