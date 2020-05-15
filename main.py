import os

BOARD_LEN = 3

board = [[0] * (BOARD_LEN ** 2) for i in range(BOARD_LEN ** 2)]
meta_board = [0] * BOARD_LEN

# variable size tic tac toe board
def generate_win_positions(length):
    horz_wins = [[i for i in range(length * length) if i % length == k] for k in range(length)]
    vert_wins = [[i for i in range(length * length) if i // length == k] for k in range(length)]
    diag_win_desc = [i for i in range(0, length * length, length + 1)]
    diag_win_asc = [i for i in range(length - 1, length * length - (length - 1), length - 1)]
    win_positions = [diag_win_asc] + [diag_win_desc] + horz_wins + vert_wins
    return win_positions

# 0 if board not won
# 1 or -1 if board won, depending on who won it
def check_board_won(board, win_positions):
    for w in win_positions:
        check = [board[i] for i in w]
        if check == [1] * BOARD_LEN || check == [-1] * BOARD_LEN:
            return check[0]
    return 0

# true if player can play here, also changes board
# otherwise false so we can check win condition
def place_on_board(board, idx, pos, player):
    sub_board = board[idx]
    if sub_board[pos] == 0:
        sub_board[pos] = player
        return True
    else:
        return False


# display board more like tic tac toe
def display(board):
    board_to_print = []
    for i in range(9):
        board_to_print.append([
            board[b][r]
            for b in range((i // 3 * 3), (i // 3 * 3 + 3))
            for r in range(((i % 3) * 3), ((i % 3) * 3 + 3))
            ])
    for b in board_to_print:
        print(*b, sep=" ")

# game loop in terminal
# can play anywhere as of right now
def main():
    playing = True
    player = 1
    os.system('cls||clear')
    win_positions = generate_win_positions(BOARD_LEN)
    sub_board_pos = -1
    pos = 0

    while playing:
        display(board)
        print("player: " + str(1 if player == 1 else 2))

        try:
            sub_board_pos, pos = tuple(input("input board, position: ").split(" "))
        except ValueError:
            os.system('cls||clear')
            print("not formatted properly!")
            continue

        try:
            sub_board_pos = int(sub_board_pos)
            pos = int(pos)
        except ValueError:
            os.system('cls||clear')
            print("not a valid position!")
            continue

        if (sub_board_pos > len(board) or pos > len(board)):
            os.system('cls||clear')
            print("not a valid position!")
            continue

        if place_on_board(board[sub_board_pos], pos, player):
            if check_board_won(board[sub_board_pos], win_positions) != 0 and meta_board[sub_board_pos] == 0:
                meta_board[sub_board_pos] = player

                if check_board_won(meta_board, win_positions) != 0:
                    os.sytem('cls||clear')
                    print("player {} won board {} and the game!", player, sub_board_pos)
                    playing = False
                    continue
                else:
                    os.system('cls||clear')
                    print("player {} won board {}!", player, sub_board_pos)

            player = -player
        else:
            os.system('cls||clear')
            print("invalid position!")

if __name__ == "__main__":
    main()
