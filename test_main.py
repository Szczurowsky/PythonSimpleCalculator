from calculator import Calculator


class Tests:

    def test_do1(self):
        numbers = [int(1), int(1)]
        new_calc = Calculator.do('PyTest', numbers, int(1))
        assert new_calc == 2

    def test_do2(self):
        numbers = [int(1), int(1)]
        new_calc = Calculator.do('PyTest', numbers, int(2))
        assert new_calc == 0

    def test_do3(self):
        numbers = [int(1), int(2)]
        new_calc = Calculator.do('PyTest', numbers, int(3))
        assert new_calc == 2

    def test_do4(self):
        numbers = [int(1), int(2)]
        new_calc = Calculator.do('PyTest', numbers, int(4))
        assert new_calc == 0.5
