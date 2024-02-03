# დაწერეთ თამაში Tic-Tac-Toe

import random
import os

board  = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def printBoard():
    os.system('cls||clear')
    for x in range(3):
        print("\n+---+---+---+")
        print("|", end="")
        for y in range(3):
            print("",board[x][y], end=" |")
    print("\n+---+---+---+")

def changeBoard(number, turn):
    if number == 1:
        board[0][0] = turn
    elif number == 2:
        board[0][1] = turn
    elif number == 3:
        board[0][2] = turn
    elif number == 4:
        board[1][0] = turn
    elif number == 5:
        board[1][1] = turn
    elif number == 6:
        board[1][2] = turn
    elif number == 7:
        board[2][0] = turn
    elif number == 8:
        board[2][1] = turn
    elif number == 9:
        board[2][2] = turn
    
    printBoard()
    
def cpuMove():
    if board[0][0] == "O" and board[0][1] == "O" and board[0][2] != "X":
        num = 3
    elif board[0][0] == "O" and board[0][2] == "O" and board[0][1] != "X":
        num = 2
    elif board[0][1] == "O" and board[0][2] == "O" and board[0][0] != "X":
        num = 1
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] != "X":
        num = 7
    elif board[0][0] == "O" and board[2][0] == "O" and board[1][0] != "X":
        num = 4
    elif board[1][0] == "O" and board[2][0] == "O" and board[0][0] != "X":
        num = 1
    elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] != "X":
        num = 6
    elif board[1][0] == "O" and board[1][2] == "O" and board[1][1] != "X":
        num = 5
    elif board[1][1] == "O" and board[1][2] == "O" and board[1][0] != "X":
        num = 4
    elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] != "X":
        num = 9
    elif board[2][0] == "O" and board[2][2] == "O" and board[2][1] != "X":
        num = 8
    elif board[2][1] == "O" and board[2][2] == "O" and board[2][0] != "X":
        num = 7
    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] != "X":
        num = 8
    elif board[0][1] == "O" and board[2][1] == "O" and board[1][1] != "X":
        num = 5
    elif board[1][1] == "O" and board[2][1] == "O" and board[0][1] != "X":
        num = 2
    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] != "X":
        num = 9
    elif board[0][2] == "O" and board[2][2] == "O" and board[1][2] != "X":
        num = 6
    elif board[1][2] == "O" and board[2][2] == "O" and board[0][2] != "X":
        num = 3
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] != "X":
        num = 9
    elif board[0][0] == "O" and board[2][2] == "O" and board[1][1] != "X":
        num = 5
    elif board[1][1] == "O" and board[2][2] == "O" and board[0][0] != "X":
        num = 1
    elif board[2][0] == "O" and board[1][1] == "O" and board[0][2] != "X":
        num = 3
    elif board[2][0] == "O" and board[0][2] == "O" and board[1][1] != "X":
        num = 5
    elif board[1][1] == "O" and board[0][2] == "O" and board[2][0] != "X":
        num = 7
    elif board[0][0] == "X" and board[0][1] == "X" and board[0][2] != "O":
        num = 3
    elif board[0][0] == "X" and board[0][2] == "X" and board[0][1] != "O":
        num = 2
    elif board[0][1] == "X" and board[0][2] == "X" and board[0][0] != "O":
        num = 1
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] != "O":
        num = 7
    elif board[0][0] == "X" and board[2][0] == "X" and board[1][0] != "O":
        num = 4
    elif board[1][0] == "X" and board[2][0] == "X" and board[0][0] != "O":
        num = 1
    elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] != "O":
        num = 6
    elif board[1][0] == "X" and board[1][2] == "X" and board[1][1] != "O":
        num = 5
    elif board[1][1] == "X" and board[1][2] == "X" and board[1][0] != "O":
        num = 4
    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] != "O":
        num = 9
    elif board[2][0] == "X" and board[2][2] == "X" and board[2][1] != "O":
        num = 8
    elif board[2][1] == "X" and board[2][2] == "X" and board[2][0] != "O":
        num = 7
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] != "O":
        num = 8
    elif board[0][1] == "X" and board[2][1] == "X" and board[1][1] != "O":
        num = 5
    elif board[1][1] == "X" and board[2][1] == "X" and board[0][1] != "O":
        num = 2
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] != "O":
        num = 9
    elif board[0][2] == "X" and board[2][2] == "X" and board[1][2] != "O":
        num = 6
    elif board[1][2] == "X" and board[2][2] == "X" and board[0][2] != "O":
        num = 3
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] != "O":
        num = 9
    elif board[0][0] == "X" and board[2][2] == "X" and board[1][1] != "O":
        num = 5
    elif board[1][1] == "X" and board[2][2] == "X" and board[0][0] != "O":
        num = 1
    elif board[2][0] == "X" and board[1][1] == "X" and board[0][2] != "O":
        num = 3
    elif board[2][0] == "X" and board[0][2] == "X" and board[1][1] != "O":
        num = 5
    elif board[1][1] == "X" and board[0][2] == "X" and board[2][0] != "O":
        num = 7
    else:
        num = random.choice(numbers)
    
    numbers.remove(num)
    changeBoard(num, "O")
    print(f"\nComputer's choise is {num}")

def winsPerson():
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
        return True
    elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
        return True
    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
        return True
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        return True
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        return True
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        return True
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        return True
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        return True
    
def winsComputer():
    if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
        return True
    elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
        return True
    elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
        return True
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
        return True
    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
        return True
    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
        return True
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        return True
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        return True

playing = True
move = 0

while playing:
    if move % 2 == 0:
        num = int(input(f"Please, input number between {numbers}: "))
        if num in numbers:
            numbers.remove(num)
            changeBoard(num, "X")
        else:
            print("Please, input valid number!")
            continue
        move += 1
    else:
        cpuMove()
        move += 1
        
    if winsPerson():
        print("You Win!")
        playing = False
    elif winsComputer():
        print("Computer Wins!")
        playing = False
    elif len(numbers) == 0:
        print("It's draw!")
        playing = False