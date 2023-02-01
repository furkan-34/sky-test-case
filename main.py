from collections import namedtuple


def square_root(number, approx_value=None):
    approx_value = approx_value if approx_value else number/2
    while True:
        quotient = number / approx_value
        new_approx = (approx_value + quotient) / 2
        if approx_value == new_approx:
            return round(new_approx, 6)
        approx_value = new_approx


input_list = [159, 3400, 67, 598, 8999]
Calculation = namedtuple("Calculation", ("value", "squareRoot"))

question_1a_answer = square_root(input_list[0])
question_1b_answer = [square_root(i) for i in input_list]
question_1c_answer = [Calculation(i, square_root(i)) for i in input_list]

class SquareRoot:
    def __init__(self, value, approx_value):
        self.value = value
        self.approx_value = approx_value
        self.calculate_square_root = square_root(value, approx_value)


question_2_answer = SquareRoot(159,12)
