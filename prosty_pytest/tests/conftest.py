import pytest

from prosty_pytest.src.lista_rzeczy import ListaRzeczyDoZrobienia


@pytest.fixture
def pusta_lista_rzeczy():
    test_obj = ListaRzeczyDoZrobienia()
    return test_obj


@pytest.fixture
def lista_rzeczy_same_do_zrobienia(request):
    test_obj = ListaRzeczyDoZrobienia()
    for rzecz in request.param:
        test_obj.dodaj_rzecz_do_zrobienia(rzecz)
    return test_obj
