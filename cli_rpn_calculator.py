import argparse
from collections import deque

stack = deque()


def check_user_expression() -> list:
    """This function will receive user's expression and return the list of
    tokens, or end the program execution if "q" command is received"""
    expression = input("Please enter Your expression: ")
    tokens = expression.split()
    if tokens == ['q']:
        raise EOFError
    return tokens


def calculation(tokens: list):
    """This function will perform the final calculations based on the received
    expression"""
    operations = {
        "+": (lambda a, b: a + b),
        "-": (lambda a, b: a - b),
        "*": (lambda a, b: a * b),
        "/": (lambda a, b: a / b)
    }
    stack.clear() if stack == deque([0.0]) else None
    try:
        for token in tokens:
            if token in operations:
                second_number, first_number = stack.pop(), stack.pop()
                result = operations[token](first_number, second_number)
                stack.append(round(float(result), 2))
            else:
                stack.append(round(float(token), 2))
        stack_str = [str(num) for num in stack]
        return ", ".join(stack_str)
    except ZeroDivisionError:
        return f'Please never divide by zero!'
    except IndexError:
        return f'Amount of operators should be less than amount of numbers!'
    except ValueError:
        return f'Please enter only numbers and operators "+, -, * or /"'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='''This is the simple CLI calculator based on 
        Reverse Polish Notation system.
        You can enter only numbers and one of the four available operators 
        (+, -, * or /).
        For example: 1 2 5 9 + * /
        and output will be: 0.04. Also You can enter your expression by parts.
        For example: Input: 5, Output: 5.0; Input: 3, Output: 5.0 3.0;
        Input: +, Output: 8.0 (5.0 + 3.0). Have fun!''')
    args = parser.parse_args()

    while True:
        try:
            print(calculation(check_user_expression()))
        except EOFError:
            print(f'Program ended')
            break
