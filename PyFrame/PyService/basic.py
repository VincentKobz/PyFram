import re
from math import *

from PyService.tools import *

def process_basic(expression):
    if not check_if_valid(expression):
        return None

    expression = re.split('([^0-9.])', expression)

    while '' in expression:
        expression.remove('')

    return evaluate_polish(convert_polish(expression))

def get_precedence(operator):
    if operator == '^':
        return 3
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '+' or operator == '-':
        return 1

def convert_polish(expression):
    operator, output, q = "-+/*^", [], []

    for elt in expression:
        if is_float(elt) or is_integer(elt):
            output.append(elt)
        elif elt in operator:
            while len(q) != 0 and (q[-1] in operator or q[-1] == ')') and get_precedence(q[-1]) >= get_precedence(elt):
                output.append(q.pop())

            q.append(elt)
        elif elt == '(':
            q.append(elt)
        elif elt == ')':
            while len(q) != 0 and q[-1] != '(':
                output.append(q.pop())

            if len(q) == 0:
                return None
            q.pop()

    while len(q) != 0:
        if q[-1] not in operator:
            return None
        output.append(q.pop())

    return output

def evaluate_polish(expression):
    if expression == None:
        return None

    stack, operator = [], "-+/*^"

    for elt in expression:
        if is_float(elt) or is_integer(elt):
            stack.append(elt)
        elif elt in operator:
            if len(stack) < 2:
                return None
            a, b, res = stack.pop(), stack.pop(), 0

            if is_float(a):
                a = convert_to_float(a)
            else:
                a = convert_to_integer(a)

            if is_float(b):
                b = convert_to_float(b)
            else:
                b = convert_to_integer(b)

            if elt == '+':
                res = a + b
            elif elt == '-':
                res = b - a
            elif elt == '/':
                if a == 0:
                    return None
                res = b / a
            elif elt == '*':
                res = a * b
            elif elt == '^':
                res = pow(b, a)
                
            stack.append(res)
    if len(stack) != 1:
        return None
    return stack.pop()

def check_if_valid(expression):
    data = ".1234567890-+/*()^"

    for i in expression:
        if i not in data:
            return False

    return True
