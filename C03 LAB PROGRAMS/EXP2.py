board = [" "] * 9

def show():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

for turn in range(9):
    show()
    p = "X" if turn % 2 == 0 else "O"
    pos = int(input(f"{p} position (1-9): ")) - 1

    if board[pos] != " ":
        print("Already taken!")
        continue

    board[pos] = p

    for a, b, c in [(0,1,2),(3,4,5),(6,7,8),
                    (0,3,6),(1,4,7),(2,5,8),
                    (0,4,8),(2,4,6)]:
        if board[a] == board[b] == board[c] != " ":
            show()
            print(p, "wins!")
            exit()

show()
print("Draw!")