binaryNumber = '1100'
binary = list(binaryNumber)
binary.reverse()

def DecimalToBinary(DeciNumber,NumberofBits):
    binaryOutput = []
    for i in range(NumberofBits):
        helpNumber = DeciNumber % 2
        DeciNumber = DeciNumber // 2
        NumbertoString = str(helpNumber)
        binaryOutput.append(NumbertoString)
    binaryOutput.reverse()
    return ''.join(binaryOutput)


def BinaryToDecimal(BinNumber):
    decimalNumber = 0
    for i in range(len(BinNumber)):
        helpNumber = decimalNumber + int(BinNumber[i]) * (2**i)
        decimalNumber = helpNumber
    return decimalNumber

print (DecimalToBinary(15,16))