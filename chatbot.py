print("muje ek tic tap game bnado")
# create a simple o,x game
# playing simple 3D game and

print("hello world")
print("game ka name tic tap")
print("playing isliye mobile")

# tic tap Game ke Variables
print("game playing har win ke baad")

# Game Board
board = ["", "", "", "", "", "", "", "", ""]

def print_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-++-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-++-")
    print(board[6] + "|" + board[7] + "|" + board[8])

def check_win(player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],  # rows
        [0,3,6],[1,4,7],[2,5,8],  # columns
        [0,4,8],[2,4,6]           # diagonals
    ]
    for combo in wins:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            print("game playing har win ke baad")
            return True
    return False

current_player = "X"

for turn in range(9):
    print_board()
    move = int(input("Player " + current_player + " position chuno (1-9): ")) - 1
    board[move] = current_player
    if check_win(current_player):
        print_board()
        print("Player " + current_player + " jeet gaya!")
        break
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"
else:
    print_board()
    print("Draw! Koi nahi jeeta.")
