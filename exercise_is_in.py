# Use bisection method to search right character in string
def isIn(char, aStr):
    # first to check that string is not none
    if aStr == '':
        return False
    # check that char is in the middle of string or not
    midNum = len(aStr)//2
    midChar = aStr[midNum]
    if char == midChar:
        return True

    elif char < midChar:
        return isIn(char, aStr[:midNum])
    else:
        return isIn(char, aStr[midNum:])