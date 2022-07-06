import argparse

operations = {
    "+": (lambda a, b: a + b),
    "-": (lambda a, b: a - b),
    "*": (lambda a, b: a * b),
    "/": (lambda a, b: a / b)
}

stack = []


def input_user_expression():
    """This function will receive the user's expression and end the program
    execution if it will receive "q" command or an end of input indicator """
    try:
        expression = input("Please enter Your expression: ")
        if expression == 'q':
            print(f'Thank You! See you next time!')
        else:
            return user_input_validation(expression)
    except EOFError:
        print(f'Program has been ended by force')


def user_input_validation(user_input: str):
    """This function will validate user's input. User's expression should
    contain some numbers (int or float) and one of the four available
    operators (+, -, * or /). Because our program stores the results of past
    calculations there is the option to input only one number or operator
    (in case there are two numbers stored in stack already)"""
    validation_list = []
    tokens = user_input.split()
    try:
        for token in tokens:
            validation_list.append(round(float(token), 2)) \
                if token not in operations else validation_list.append(token)
    except ValueError:
        print(f'Please enter only numbers and operators "+, -, * or /"')
        return input_user_expression()
    if validation_list[0] in operations and len(stack) <= 1:
        print("Please enter at least two numbers before operator")
        return input_user_expression()
    return calculation(tokens)


def calculation(list_of_tokens: list) -> float:
    """This function will perform the final calculations based on the received
    validated tokens"""
    try:
        for token in list_of_tokens:
            if token in operations:
                second_number = stack.pop()
                first_number = stack.pop()
                result = operations[token](first_number, second_number)
                stack.append(round(float(result), 2))
            else:
                stack.append(round(float(token), 2))
        print(*stack)
        return input_user_expression()
    except IndexError:
        print(f'Amount of operators should be less than amount of numbers!')


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

input_user_expression()

