from math import *
from PyService.tools import *

def Normalize(expression):
    expression, norm, result = expression.split(","), 0, []

    for elt in expression:
        print(elt)
        if not isFloat(elt) and not isInteger(elt):
            print('test')
            return None

        norm += float(elt) * float(elt)
    norm = ["sqrt(", str(norm), ")"]

    for elt in expression:
        result.append("".join([elt, " / ", norm[0], norm[1], norm[2]]))

    return "{ " + ", ".join(result) + " }"