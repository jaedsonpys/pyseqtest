import pyseqtest


class TestCalculator(pyseqtest.SeqTest):
    def __init__(self):
        super().__init__()

    def test_sum(self):
        condition = (10 + 5) == 15
        self.is_true(condition)

    def test_multiplication(self):
        condition = (2 * 5) == 10
        self.is_true(condition)

    def test_division(self):
        # error demonstration
        condition = (10 / 2) == 90
        self.is_true(condition, msg_error='Oh, the result is wrong')


if __name__ == '__main__':
    TestCalculator().run()
