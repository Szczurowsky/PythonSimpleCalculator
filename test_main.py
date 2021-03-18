from main import Calculator


def test_do():
    numbers = [int(1), int(1)]
    new_calc = Calculator.do('PyTest', numbers, int(1))
    assert new_calc == 2
