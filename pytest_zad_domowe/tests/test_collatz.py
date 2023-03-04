"""Napisz testy dla collatz_conjecture
komenda:
...PycharmProjects/wsb_python>  pytest -vs --cov pytest_zad_domowe.src --cov-report term-missing ./pytest_zad_domowe/tests/
Spróbuj osiągnąć 100% pokrycia kodu!
"""
import pytest
from pytest_zad_domowe.src.collatz import collatz_conjecture, CollatzBadNumberError


@pytest.mark.parametrize("n, expected", [
    (3, [3, 10, 5, 16, 8, 4, 2, 1]),
    (7, [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]),
],
                         ids=["3", "7"])
def test_collatz(n: int, expected: list[int]):
    assert collatz_conjecture(n) == expected


def test_collatz_negative():
    with pytest.raises(CollatzBadNumberError):
        collatz_conjecture(-21)
