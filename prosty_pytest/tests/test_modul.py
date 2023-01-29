import pytest
from prosty_pytest.src.modul import divide


@pytest.mark.parametrize(
    "a, b, expected_result",
    [
        [12, 2, 6],
        [4, -4, -1]
    ]
)
def test_divide(a, b, expected_result):
    result = divide(a, b)
    assert result == expected_result, \
        f"function add with params 5 and 7 should have returned 12! Actual result: {result}"


def test_divide_negative():
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
    # try:
    #     divide(5, 0)
    # except ZeroDivisionError:
    #     print("Tak miało być :D")
    # else:
    #     raise AssertionError("Divide miał sie wywalić :<")
