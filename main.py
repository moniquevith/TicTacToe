from helper import drawBoard

print("--------Welcome to Noughts & Crosses ------------- \nCreated by: Monique Vith")
print("--------------------------------------------------")
spots = [[1,2,3],[4,5,6],[7,8,9]]
drawBoard(spots)

def checkWinner(spots): 
    for row in range(3):
        for col in range(3):
            print("to be done")

winner = False
player = 1 # if player 1: X, player 2: O``
while (not winner):
    val = input(f"Player {player} pick your move: ")
    if player == 1:
        for row in range(3):
            for col in range(3):
                if (spots[row][col] == int(val)): # if spot isnt taken 
                    spots[row][col] = 'X'
                    break
                if (spots[row][col] == 'O'): # if spot is taken
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
                if (spots[row][col] == 'X'): # if spot is taken
                    val = input("Spot has been taken, choose another move: ")
                    continue
        drawBoard(spots)
        player = 1
    
    checkWinner(spots)
