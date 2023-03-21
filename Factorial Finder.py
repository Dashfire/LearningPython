def Factorial1(Input):
    if Input == 0 or Input == 1:
        return 1
    else:
        return Input * Factorial1(Input-1)