class ListaRzeczyDoZrobienia:
    def __init__(self):
        self.lista_rzeczy_do_zrobienia = []
        self.lista_rzeczy_zrobionych = []

    def dodaj_rzecz_do_zrobienia(self, rzecz):
        self.lista_rzeczy_do_zrobienia.append(rzecz)

    def oznacz_rzecz_jako_zrobiona(self, indeks):
        self.lista_rzeczy_zrobionych.append(self.lista_rzeczy_do_zrobienia[indeks])
        del self.lista_rzeczy_do_zrobienia[indeks]

    def pokaz_rzeczy(self):
        output = ['Do zrobienia jest: ']
        for indeks, rzeczy_do_zrobienia in enumerate(self.lista_rzeczy_do_zrobienia):
            output.append(f'\t\t{indeks} [ ] {rzeczy_do_zrobienia}')
        output.append('Zrobione jest: ')
        for indeks, rzeczy_do_zrobienia in enumerate(self.lista_rzeczy_zrobionych):
            output.append(f'\t\t{indeks} [x] {rzeczy_do_zrobienia}')
        return "\n".join(output)

    def usun_rzecz_do_zrobienia(self, indeks):
        del self.lista_rzeczy_do_zrobienia[indeks]

    def ustaw_rzecz_na_poczatek(self, indeks):
        element_na_poczatek = self.lista_rzeczy_do_zrobienia[indeks]
        del self.lista_rzeczy_do_zrobienia[indeks]
        self.lista_rzeczy_do_zrobienia.insert(0, element_na_poczatek)

    def oznacz_rzecz_zrobiona_jako_niezrobiona(self, indeks):
        self.lista_rzeczy_do_zrobienia.append(self.lista_rzeczy_zrobionych[indeks])
        del self.lista_rzeczy_zrobionych[indeks]
