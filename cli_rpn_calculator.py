import argparse

operations = {
    "+": (lambda a, b: a + b),
    "-": (lambda a, b: a - b),
    "*": (lambda a, b: a * b),
    "/": (lambda a, b: a / b)
}

stack = []


def input_user_expression():
    """This function will receive user's expression and send it
    to validation"""
    expression = input("Please enter Your expression: ")
    tokens = expression.split()
    return end_of_program_check(tokens)


def end_of_program_check(tokens: list):
    """This function will end the program execution if received "q" command
    or an end of input indicator"""
    if tokens == ['q']:
        raise EOFError
    else:
        return user_input_validation(tokens)


def user_input_validation(tokens: list):
    """This function will validate user's expression to make sure the user
    has entered only numbers and available operators"""
    validation_list = []
    try:
        for token in tokens:
            validation_list.append(round(float(token), 2)) \
                if token not in operations else validation_list.append(token)
    except ValueError:
        return 'Please enter only numbers and operators "+, -, * or /"'
    return check_numbers_and_operators_amount(tokens)


def check_numbers_and_operators_amount(tokens: list):
    """This function will check amount of entered numbers and operators.
    Since the program saves the results of previous inputs and operations,
    we should be sure that amount of operators is not greater than the amount
    of numbers and that we have at least two numbers to perform calculation"""
    numbers_list = []
    operators_list = []
    for token in tokens:
        if token not in operations:
            numbers_list.append(token)
        else:
            operators_list.append(token)
    total_numbers_list = numbers_list + stack
    if (len(total_numbers_list) - len(operators_list)) < 1:
        return 'Amount of operators should be less than amount of numbers!'
    return calculation(tokens)


def calculation(tokens: list):
    """This function will perform the final calculations based on the received
    validated tokens"""
    stack.clear() if stack == [0.0] else None
    try:
        for token in tokens:
            if token in operations:
                second_number = stack.pop()
                first_number = stack.pop()
                result = operations[token](first_number, second_number)
                stack.append(round(float(result), 2))
            else:
                stack.append(round(float(token), 2))
        stack_str = [str(num) for num in stack]
        return ", ".join(stack_str)
    except ZeroDivisionError:
        return f'Please never divide by zero!'


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
            print(input_user_expression())
        except EOFError:
            print(f'Program ended')
            break
