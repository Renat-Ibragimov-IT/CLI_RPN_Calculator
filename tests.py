import unittest
from cli_rpn_calculator import end_of_program_check, user_input_validation, \
    check_numbers_and_operators_amount, calculation


class TestEndOfProgramCheck(unittest.TestCase):
    def test_q_command(self):
        with self.assertRaises(EOFError):
            end_of_program_check(['q'])

    def test_another_input(self):
        actual = end_of_program_check(['5', 'fgfgff', '+'])
        expected = user_input_validation(['5', 'fgfgff', '+'])
        self.assertEqual(actual, expected)


class TestUserInputValidation(unittest.TestCase):
    def test_incorrect_user_input(self):
        actual = user_input_validation(['hjbhjbhjb', 'hjbhjb', '+'])
        expected = 'Please enter only numbers and operators "+, -, * or /"'
        self.assertEqual(actual, expected)

    def test_correct_user_input(self):
        actual = user_input_validation(['1', '2', '+', '+'])
        expected = check_numbers_and_operators_amount(['1', '2', '+', '+'])
        self.assertEqual(actual, expected)


class TestCheckNumbersAndOperatorsAmount(unittest.TestCase):
    def test_check_incorrect_numbers_and_operators_amount(self):
        actual = check_numbers_and_operators_amount(['5', '2', '+', '-'])
        expected = 'Amount of operators should be less than amount of numbers!'
        self.assertEqual(actual, expected)


class TestCalculation(unittest.TestCase):
    def test_expressions_true(self):
        actual = calculation(['1', '2', '3', '4', '5', '/', '*', '-', '+'])
        expected = '0.6'
        self.assertEqual(actual, expected)

    def test_zero_division(self):
        actual = calculation(['0', '/'])
        expected = 'Please never divide by zero!'
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
