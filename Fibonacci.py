def Fibo1(x):
    if x == 1 or x == 2:
        return 1
    else:
        return Fibo1(x-1) + Fibo1(x-2)
    
def Fibo2(x):
    Num1 = 0
    Num2 = 1
    for i in range(x-1):
        Num3 = Num1 + Num2
        Num1 = Num2
        Num2 = Num3
    return Num3