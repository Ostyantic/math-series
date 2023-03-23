from modules.series import fibonacci

from modules.series import lucas

from modules.series import sum_series


# fibonacci test 1
def test_fibonacci_exists():
    assert fibonacci()


# fibonacci test 2
def test_fibonacci_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


# fibonacci test 3
def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


# fibonacci test 4
def test_fibonacci_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


# fibonacci test 5
def test_fibonacci_five():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected


# fibonacci test 6
def test_fibonacci_eleven():
    actual = fibonacci(11)
    expected = 89
    assert actual == expected


# fibonacci test 7
def test_fibonacci_negative():
    actual = fibonacci(-1)
    expected = 0
    assert actual == expected


# lucas test 1
def test_lucas_exists():
    assert lucas(0)


# lucas test 2
def test_lucas_zero():
    actual = lucas(0)
    expected = 2
    assert actual == expected


# lucas test 3
def test_lucas_one():
    actual = lucas(1)
    expected = 1
    assert actual == expected


# lucas test 5
def test_lucas_five():
    actual = lucas(5)
    expected = 11
    assert actual == expected


# lucas test 6
def test_lucas_fifteen():
    actual = lucas(15)
    expected = 1364
    assert actual == expected


# lucas test 7
def test_lucas_negative():
    actual = lucas(-1)
    expected = 2
    assert actual == expected


def test_sum_series_exists():
    assert sum_series(1)

