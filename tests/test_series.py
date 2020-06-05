from math_series import __version__
from math_series.series import fibonacci
from math_series.series import lucas


def test_version():
    assert __version__ == '0.1.0'


def test_fibonacci1():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fibonacci2():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fibonacci3():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_fibonacci4():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected


def test_fibonacci5():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected


def test_fibonacci6():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected


def test_lucas1():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_lucas2():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_lucas3():
    actual = lucas(2)
    expected = 3
    assert actual == expected


def test_lucas4():
    actual = lucas(3)
    expected = 4
    assert actual == expected


def test_lucas5():
    actual = lucas(4)
    expected = 7
    assert actual == expected


def test_lucas6():
    actual = lucas(5)
    expected = 11
    assert actual == expected
