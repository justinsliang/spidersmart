tttBoard = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]

def printBoard():
    for i in range(0, 3):
        print(tttBoard[i])

def checkWin():
    #rows
    for r in range(0, 3):
        if (tttBoard[r][0] == tttBoard[r][1]) and (tttBoard[r][0] == tttBoard[r][2]):
            return tttBoard[r][0]

    #column
    for c in range(0, 3):
        if (tttBoard[0][c] == tttBoard[1][c]) and (tttBoard[0][c] == tttBoard[2][c]):
            return tttBoard[0][c]

    #diagonals
    if (tttBoard[0][0] == tttBoard[1][1]) and (tttBoard[0][0] == tttBoard[2][2]):
        return tttBoard[0][0]
    if (tttBoard[0][2] == tttBoard[1][1]) and (tttBoard[0][2] == tttBoard[2][0]):
        return tttBoard[0][0]
    
    return "!"

print("Welcome to Tic Tac Toe")

option = ""
player = "O"

while option != "0":
    print("1: PVP")
    print("2: vs AI")
    print("0: Exit")
    option = input("Select a gamemode: ")

    if option == "1": 
        while checkWin() == "!":
            printBoard()
            row = int(input("Enter the row: "))
            col = int(input("Enter the column: "))
            tttBoard[row][col] = player
            if player == "O":
                player = "X"
            else: 
                player = "O"
        
