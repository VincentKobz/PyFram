import re

from PyFrame.PyService.tools import is_float, is_integer

def process_percentage(expression):
    exp = "".join(expression.split())

    percentage_reg, counter, actual, percentage, value = re.compile('^[0-9]+%$'), 0, "", "", ""

    for i in range (len(exp)):

        actual = actual + exp[i]

        if percentage_reg.match(actual) and counter == 0:
            percentage, counter, actual = actual[:-1], counter + 1, ""
        elif actual == "of" and counter == 1:
            counter, actual = counter + 1, ""
        elif (is_float(actual) or is_integer(actual)) and counter == 2:
            if i < len(exp) and not is_float(actual + exp[i + 1]) and not is_integer(actual + exp[i + 1]):
                value = actual
                counter, actual = counter + 1, ""

    if counter != 3:
        return None

    return  str((int(value) / 100) * int(percentage)) + " " + actual