def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def isInteger(string):
    try:
        int(string)
        return True
    except ValueError:
        return False

def convertToFloat(string):
    try:
        return float(string)
    except ValueError:
        return None

def convertToInteger(string):
    try:
        return int(string)
    except ValueError:
        return None