binaryNumber = '1100'
binary = list(binaryNumber)
binary.reverse()

def DecimalToBinary(deciNumber,amountOfBits):
    binaryOutput = []
    for i in range(amountOfBits):
        helpNumber = deciNumber % 2
        deciNumber = deciNumber // 2
        numberToString = str(helpNumber)
        binaryOutput.append(numberToString)
    binaryOutput.reverse()
    return ''.join(binaryOutput)


def BinaryToDecimal(binNumber):
    decimalNumber = 0
    for i in range(len(binNumber)):
        helpNumber = decimalNumber + int(binNumber[i]) * (2**i)
        decimalNumber = helpNumber
    return decimalNumber