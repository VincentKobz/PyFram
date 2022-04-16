import re
from math import *

from PyService.tools import *

def Basic(expression):
    if not checkIfValid(expression):
        return None

    expression = re.split('([^0-9.])', expression)

    while '' in expression:
        expression.remove('')

    return evaluatePolish(convertPolish(expression))

def getPrecedence(operator):
    if operator == '^':
        return 3
    elif operator == '*' or operator == '/':
        return 2
    elif operator == '+' or operator == '-':
        return 1

def convertPolish(expression):
    operator, output, q = "-+/*^", [], []

    for elt in expression:
        if isFloat(elt) or isInteger(elt):
            output.append(elt)
        elif elt in operator:
            while len(q) != 0 and (q[-1] in operator or q[-1] == ')') and getPrecedence(q[-1]) >= getPrecedence(elt):
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

def evaluatePolish(expression):
    if expression == None:
        return None

    stack, operator = [], "-+/*^"

    for elt in expression:
        if isFloat(elt) or isInteger(elt):
            stack.append(elt)
        elif elt in operator:
            if len(stack) < 2:
                return None
            a, b, res = stack.pop(), stack.pop(), 0

            if isFloat(a):
                a = convertToFloat(a)
            else:
                a = convertToInteger(a)

            if isFloat(b):
                b = convertToFloat(b)
            else:
                b = convertToInteger(b)

            if elt == '+':
                res = a + b
            elif elt == '-':
                res = b - a
            elif elt == '/':
                res = b / a
            elif elt == '*':
                res = a * b
            elif elt == '^':
                res = pow(b, a)
                
            stack.append(res)
    if len(stack) != 1:
        return None
    return stack.pop()

def checkIfValid(expression):
    data = ".1234567890-+/*()^"

    for i in expression:
        if i not in data:
            return False

    return True
