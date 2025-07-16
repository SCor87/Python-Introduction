num1 = input("Enter any number:")
firstNumber = input("Enter start number:")
lastNumber = input("Enter last number:")

A = int(firstNumber)
while A<=int(lastNumber):
    print(num1, "x", A, "=", A*int(num1))
    A = A + 1