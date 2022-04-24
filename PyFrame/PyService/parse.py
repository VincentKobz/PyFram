from PyFrame.PyService import percentage
from PyService import normalize
from PyService import basic
from PyService import function
from math import *


def parser(calcul):
    print(calcul)
    expression = calcul.split(':')

    if len(expression) < 2:
        return None

    header, exp = expression[0], expression[1]
    exp = "".join(exp.split())
    if header == 'basic' and len(expression) == 2:
        return basic.process_basic(exp)
    elif header == 'normalize' and len(expression) == 2:
        return normalize.process_normalize(exp)
    elif header == 'function' and len(expression) == 3:
        return function.process_function(exp, expression[2])
    elif header == 'sqrt' and len(expression) == 2:
        if not exp.isnumeric():
            return None
    
        return sqrt(radians(int(exp)))
    elif header == 'percentage' and len(expression) == 2:
        return percentage.process_percentage(exp)
    elif header == 'cos' and len(expression) == 2:
        if not exp.isnumeric():
            return None

        return cos(radians(int(exp)))
    elif header == 'sin' and len(expression) == 2:
        if not exp.isnumeric():
            return None

        return sin(radians(int(exp)))
    elif header == 'arcsin' and len(expression) == 2:
        if not exp.isnumeric():
            return None

        return asin(radians(int(exp)))
    elif header == 'arccos' and len(expression) == 2:
        if not exp.isnumeric():
            return None

        return acos(radians(int(exp)))
    return None