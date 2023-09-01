def Collatz (Input: int, Depth = 0):
    if Input == 1:
        return Depth
    else:
        if Input % 2 == 0:
            return (Collatz(Input / 2, Depth+1))
        else:
            return (Collatz(Input * 3 + 1, Depth+1))
        

Input = input("Type an Integer: ")
print ("The Number of Steps to 1 are", Collatz(int(Input)))