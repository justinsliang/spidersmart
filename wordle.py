import random
from wordlewordlist import wordleWordList 

#write some code to pick the word of the day
wodList = [" ", " ", " ", " ", " "]
wodIndex = random.randint(0, 2308)
wod = wordleWordList[wodIndex]
for i in range(0, 5):
    wodList[i] = wod[i]


#print game interface ****AS A FUNCTION
printList = [[" ", " ", " ", " ", " "], 
             [" ", " ", " ", " ", " "], 
             [" ", " ", " ", " ", " "], 
             [" ", " ", " ", " ", " "], 
             [" ", " ", " ", " ", " "], 
             [" ", " ", " ", " ", " "]]

allLetters = ["A", "B", "C", "D", 
              "E", "F", "G", "H", 
              "I", "J", "K", "L",
              "M", "N", "O", "P",
              "Q", "R", "S", "T",
              "U", "V", "W", "X",
              "Y", "Z"]
for i in range(0, len(allLetters)):
    allLetters[i] = allLetters[i].lower()
              
sortedUsedLetters = []

print("Welcome to Wordle")
guess = 0
option = ""
while option != "0" and guess < 6:
    outputstring = f""
    for r in range(0, 6):
        for c in range(0, 5):
            if printList[r][c] in wodList:
                if printList[r][c] == wodList[c]:
                    outputstring += f"{{{printList[r][c]}}}"
                else:
                    outputstring += f"({printList[r][c]})"
            else:
                outputstring += f"[{printList[r][c]}]"
            if printList[r][c] != " ":
                sortedUsedLetters.append(printList[r][c])
            sortedUsedLetters = sorted(list(set(sortedUsedLetters)))
        print(outputstring)
        outputstring = f""     
    
    #REMOVE AFTER TESTING
    print(wod)

    print("Used Letters: ")
    print(sortedUsedLetters)
    
    for i in range(0, len(sortedUsedLetters)):
        if sortedUsedLetters[i] in allLetters:
            allLetters.remove(sortedUsedLetters[i])

    print("Unused Letters")
    print(allLetters)

    print("0: quit")
    print("1: guess")
    option = input("Choose an option: ")

    if option == "1":
        userinput = ""
        while len(userinput) != 5:
            userinput = input("Enter your guess: ")
            if userinput not in wordleWordList:
                print("That is not a valid word")
                userinput = ""  
        for i in range(0, 5):
            printList[guess][i] = userinput[i]
        guess += 1

outputstring = f""
for r in range(0, 6):
    for c in range(0, 5):
        if printList[r][c] in wodList:
            if printList[r][c] == wodList[c]:
                outputstring += f"{{{printList[r][c]}}}"
            else:
                outputstring += f"({printList[r][c]})"
        else:
            outputstring += f"[{printList[r][c]}]"
        if printList[r][c] != " ":
            sortedUsedLetters.append(printList[r][c])
        sortedUsedLetters = sorted(list(set(sortedUsedLetters)))
    print(outputstring)
    outputstring = f""   

print("The correct word is: " + wod)

