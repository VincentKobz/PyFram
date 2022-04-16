from PyService import basic

def Function(expression, value):
    if not checkIfValid(expression):
        return None

    expression = expression.replace("x", value)
    expression = "".join(expression.split())

    return basic.Basic(expression)

def checkIfValid(expression):
    data = ".1234567890-+/*()^x"

    for i in expression:
        if i not in data:
            return False

    return True