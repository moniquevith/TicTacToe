from helper import drawBoard

print("--------Welcome to Noughts & Crosses ------------ \nCreated by: Monique Vith")
print("--------------------------------------------------")
spots = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
drawBoard(spots)

def checkWinner(spots):
    

winner = False
player = 1 # if player 1: X, player 2: O
turn = 'X'
while (not winner):
    val = input(f"Player {player} pick your move:")
    if player == 1:
        spots[int(val)] = "X"
        player = 2
    else:
        spots[int(val)] = "O"
        player = 1
    
    checkWinner(spots)
    drawBoard(spots)
