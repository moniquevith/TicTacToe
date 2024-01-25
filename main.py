from helper import drawBoard
import math
print("--------Welcome to Noughts & Crosses ------------- \nCreated by: Monique Vith")
print("--------------------------------------------------")
spots = [[1,2,3],[4,5,6],[7,8,9]]
drawBoard(spots)

winner = False
gameWinner = 0
player = 1 # if player 1: X, player 2: O

# could also put winning indexes in an array and iterate to get winner
def checkWinner(spots):
    for row in range(3):
        for col in range(3):
            if ((col + 2) == 2 and spots[row][col] == "X" and spots[row][col + 1] == "X" and spots[row][col + 2] == "X"): # check horizontal player 1
                gameWinner = 1
                print(f"Winner is Player {gameWinner}!")
                return True
            if ((col + 2) == 2 and spots[row][col] == "O" and spots[row][col + 1] == "O" and spots[row][col + 2] == "O"): # check horizontal player 2
                gameWinner = 2
                print(f"Winner is Player {gameWinner}!")
                return True
            if ((row + 2) == 2 and spots[row][col] == "X" and spots[row + 1][col] == "X" and spots[row + 2][col] == "X"): # check vertical player 1
                gameWinner = 1
                print(f"Winner is Player {gameWinner}!")
                return True
            if ((row + 2) == 2 and spots[row][col] == "O" and spots[row + 1][col] == "O" and spots[row + 2][col] == "O"): # check vertical player 2
                gameWinner = 2
                print(f"Winner is Player {gameWinner}!")
                return True
            if (row == col and row == 0 and col == 0 and spots[row][col] == "X" and spots[row + 1][col + 1] == "X" and spots[row + 2][col + 2] == "X"): # check diagonal left Player 1
                gameWinner = 1
                print(f"Winner is Player {gameWinner}!")
                return True
            if (row == col and row == 0 and col == 0 and spots[row][col] == "O" and spots[row + 1][col + 1] == "O" and spots[row + 2][col + 2] == "O"): # check diagonal left Player 2
                gameWinner = 2
                print(f"Winner is Player {gameWinner}!")
                return True
            if (row == col and row == 1 and col == 1 and spots[row][col] == "X" and spots[row - 1][col + 1] == "X" and spots[row + 1][col - 1] == "X"): # check diagonal right Player 1
                gameWinner = 1
                print(f"Winner is Player {gameWinner}!")
                return True
            if (row == col and row == 1 and col == 1 and spots[row][col] == "O" and spots[row - 1][col + 1] == "O" and spots[row + 1][col - 1] == "O"): # check diagonal right Player 1
                gameWinner = 2
                print(f"Winner is Player {gameWinner}!")
                return True
    return False

def checkDraw(spots):
    for row in range(3):
        if all(isinstance(idx, str) for idx in spots[row]) == False: # if any of the indexes are ints, then there are still moves left
            return False
    return True

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
    
    if (checkWinner(spots)):
        winner = True

    if (checkDraw(spots)):
        print("the game is a Draw!")
        winner = True