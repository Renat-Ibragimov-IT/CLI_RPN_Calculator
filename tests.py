import unittest
from unittest.mock import patch
from cli_rpn_calculator import calculation, check_user_expression


class TestCalculationErrors(unittest.TestCase):
    def test_zero_division(self):
        actual = calculation(['5', '0', '/'])
        expected = 'Please never divide by zero!'
        self.assertEqual(actual, expected)

    def test_index_error(self):
        actual = calculation(['5', '5', '+', '-'])
        expected = 'Amount of operators should be less than amount of numbers!'
        self.assertEqual(actual, expected)

    def test_value_error(self):
        actual = calculation(['a', '#'])
        expected = 'Please enter only numbers and operators "+, -, * or /"'
        self.assertEqual(actual, expected)


class TestCalculationExpressionTrue(unittest.TestCase):
    def test_expression_true(self):
        actual = calculation(['1', '2', '3', '4', '5', '/', '*', '-', '+'])
        expected = '0.6'
        self.assertEqual(actual, expected)


class TestUserExpression(unittest.TestCase):
    def test_user_expression(self):
        with patch('builtins.input', return_value='5 5 +'):
            self.assertEqual(check_user_expression(), ['5', '5', '+'])

    def test_q_command(self):
        with patch('builtins.input', return_value='q'):
            with self.assertRaises(EOFError) as context:
                check_user_expression()
                self.assertTrue('Program ended' in context.exception)


if __name__ == '__main__':
    unittest.main()
