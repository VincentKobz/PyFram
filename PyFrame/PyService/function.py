from PyService import basic

def process_function(expression, value):
    if not check_if_valid(expression):
        return None

    expression = expression.replace("x", value)
    expression = "".join(expression.split())

    return basic.Basic(expression)

def check_if_valid(expression):
    data = ".1234567890-+/*()^x"

    for i in expression:
        if i not in data:
            return False

    return True