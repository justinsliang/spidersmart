print("Calculator open")
print("1: Addition/Subtraction")
print("2: Multiplication")
print("3: Division")
print("4: Scientific Notation")
print("0: Exit")
option = ""
while option != "0":
    option = input("Select option: ")
    if option == "1":
        #code for addition
        numBank = []
        bankSize = int(input("How many numbers in the bank: "))
        for i in range(0, bankSize):
            numBank.append(float(input("Enter number in bank: ")))
        print("The sum is")
        print(sum(numBank))

    if option == "2":
        #code for multiplication
        numBank = []
        output = 1
        bankSize = int(input("How many numbers in the bank: "))
        for i in range(0, bankSize):
            numBank.append(float(input("Enter number in bank: ")))
            output *= numBank[i]
        print("The product is")
        print(output)

    if option == "3":
        #code for division
        numerator = float(input("What is the numerator: "))
        denom = float(input("What is the denominator: "))
        print("The quotient is")
        print(numerator / denom)

    if option == "4":
        #code for percents
        output = float(input("Number to convert: "))
        print("{:e}".format(output))
