from helper import drawBoard
import math
print("--------Welcome to Noughts & Crosses ------------- \nCreated by: Monique Vith")
print("--------------------------------------------------")
spots = [[1,2,3],[4,5,6],[7,8,9]]
drawBoard(spots)

winner = False
gameWinner = 0
player = 1 # if player 1: X, player 2: O

def checkWinner(spots): 
    for row in range(3):
        for col in range(3):
            if ((col + 2) == 2 and spots[row][col] == "X" and spots[row][col + 1] == "X" and spots[row][col + 2] == "X"): # check horizontal 
                gameWinner = 1
                winner = True  

while (not winner):
    val = input(f"Player {player} pick your move: ")
    if player == 1:
        for row in range(3):
            for col in range(3):
                if (spots[row][col] == int(val)): # if spot isnt taken 
                    spots[row][col] = 'X'
                    break
                if (spots[(int(val) - 1)//3][(int(val) - 1) % 3] == 'O'): # if spot is taken
                    val = input("Spot has been taken, choose another move: ")
                    continue
        drawBoard(spots)
        player = 2
    else:
        for row in range(3):
            for col in range(3):
                if (spots[row][col] == int(val)): # if spot isnt taken
                    spots[row][col] = 'O'
                    break
                if (spots[(int(val) - 1)//3][(int(val) - 1) % 3] == 'X'): # if spot is taken
                    val = input("Spot has been taken, choose another move: ")
                    continue
        drawBoard(spots)
        player = 1
    
    checkWinner(spots)

print(f"Winner is Player {gameWinner}!")