tttBoard = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]

def printBoard():
    for i in range(0, 3):
        print(tttBoard[i])

print("Welcome to Tic Tac Toe")

option = ""

while option != "0":
    print("1: PVP")
    print("2: vs AI")
    print("0: Exit")
    option = input("Select a gamemode: ")

    if option == "1": 
        