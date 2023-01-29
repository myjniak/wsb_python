import pytest


def test_dodaj_rzecz_do_zrobienia(pusta_lista_rzeczy):
    pusta_lista_rzeczy.dodaj_rzecz_do_zrobienia("chleb")
    assert "chleb" in pusta_lista_rzeczy.lista_rzeczy_do_zrobienia


@pytest.mark.parametrize(
    "lista_rzeczy_same_do_zrobienia",
    [
        ["chleb", "maslo"]
    ],
    indirect=True
)
def test_oznacz_rzecz_jako_zrobiona(lista_rzeczy_same_do_zrobienia):
    lista_rzeczy_same_do_zrobienia.oznacz_rzecz_jako_zrobiona(1)
    assert "maslo" in lista_rzeczy_same_do_zrobienia.lista_rzeczy_zrobionych
    assert "maslo" not in lista_rzeczy_same_do_zrobienia.lista_rzeczy_do_zrobienia


def test_oznacz_rzecz_jako_zrobiona_negative(pusta_lista_rzeczy):
    with pytest.raises(IndexError):
        pusta_lista_rzeczy.oznacz_rzecz_jako_zrobiona(1)


@pytest.mark.parametrize(
    "lista_rzeczy_same_do_zrobienia",
    [
        ["chleb", "maslo", "kolacja", "badminton"]
    ],
    indirect=["lista_rzeczy_same_do_zrobienia"]
)
def test_pokaz_rzeczy(lista_rzeczy_same_do_zrobienia):
    output = lista_rzeczy_same_do_zrobienia.pokaz_rzeczy()
    for rzecz in ["chleb", "maslo", "kolacja"]:
        assert f"[ ] {rzecz}" in output
