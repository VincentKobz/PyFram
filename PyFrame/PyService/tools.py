def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def is_integer(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def convert_to_float(string):
    try:
        value = float(string)
    except ValueError:
        return None
    else:
        return value

def convert_to_integer(string):
    try:
        value = int(string)
    except ValueError:
        return None
    else:
        return value