def Collatz (Input, Depth):
    if Input == 1:
        return Depth
    else:
        if Input % 2 == 0:
            return (Collatz(Input / 2, Depth+1))
        else:
            return (Collatz(Input * 3 + 1, Depth+1))
        


print ("The Number of Steps to 1 are", Collatz(5,0))