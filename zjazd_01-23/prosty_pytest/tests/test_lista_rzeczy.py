from src.lista_rzeczy import ListaRzeczyDoZrobienia


def test_dodaj_rzecz_do_zrobienia():
    test_obj = ListaRzeczyDoZrobienia()
    test_obj.dodaj_rzecz_do_zrobienia("chleb")
    assert "chleb" in test_obj.lista_rzeczy_do_zrobienia


def test_oznacz_rzecz_jako_zrobiona():
    test_obj = ListaRzeczyDoZrobienia()
    test_obj.dodaj_rzecz_do_zrobienia("chleb")
    test_obj.dodaj_rzecz_do_zrobienia("maslo")
    test_obj.oznacz_rzecz_jako_zrobiona(1)
    assert "maslo" in test_obj.lista_rzeczy_zrobionych
    assert "maslo" not in test_obj.lista_rzeczy_do_zrobienia


def test_pokaz_rzeczy():
    rzeczy = ["chleb", "maslo", "kolacja"]
    test_obj = ListaRzeczyDoZrobienia()
    for rzecz in rzeczy:
        test_obj.dodaj_rzecz_do_zrobienia(rzecz)
    output = test_obj.pokaz_rzeczy()
    for rzecz in rzeczy:
        assert f"[ ] {rzecz}" in output
