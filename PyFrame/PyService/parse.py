from PyService import normalize
from PyService import basic
from PyService import function
from math import *


def parser(calcul):
    calcul = calcul[1:-1]
    print(calcul)
    expression = calcul.split(':')

    if len(expression) < 2:
        return None

    header, exp = expression[0], expression[1]
    exp = "".join(exp.split())
    if header == 'basic' and len(expression) == 2:
        return basic.Basic(exp)
    elif header == 'normalize' and len(expression) == 2:
        return normalize.Normalize(exp)
    elif header == 'function' and len(expression) == 3:
        return function.Function(exp, expression[2])
    elif header == 'sqrt' and len(expression) == 2:
        if not exp.isnumeric():
            return None

        return sqrt(radians(int(exp)))
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
    elif header == 'arcos' and len(expression) == 2:
        if not exp.isnumeric():
            return None

        return acos(radians(int(exp)))

    return None