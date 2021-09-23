import time

from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
from game import TicTacToe

def play(game, x_player, o_player, is_print_game=True):
    if is_print_game:
        game.print_board_nums()

    cur_letter = "X"

    while game.has_empty_squares():
        if cur_letter == "O":
            square = o_player.get_next_move(game)
        else:
            square = x_player.get_next_move(game)

        if game.make_move(square, cur_letter):
            if is_print_game:
                print(f"[ {cur_letter} ] makes a move to square [ {square} ].")
                game.print_board()
                print("="*30)

            #### WIN ####
            if game.get_cur_winner():
                if is_print_game:
                    print(f"{cur_letter} wins!")
                return cur_letter

            # update current player
            cur_letter = "O" if cur_letter == "X" else "X"

        if is_print_game:
            time.sleep(1)

    #### TIE ####
    if is_print_game:
        print("It's a tie!")

# if __name__ == "__main__":
#     x_player = HumanPlayer("X")
#     o_player = GeniusComputerPlayer("O")

#     t = TicTacToe(size=4)

#     play(t, x_player, o_player, is_print_game=True)

# simulation
if __name__ == "__main__":
    x_wins, o_wins, ties = 0, 0, 0
    iter = 100

    for i in range(iter):
        print(f"\r{i+1:{len(str(iter))}d}/{iter}", end="")

        x_player = RandomComputerPlayer("X")
        o_player = GeniusComputerPlayer("O")

        t = TicTacToe(size=3) # bigger size will take forever

        result = play(t, x_player, o_player, is_print_game=False)

        if result == "X":
            x_wins += 1
        elif result == "O":
            o_wins += 1
        else:
            ties += 1

    print(f"\nAfter {iter} iterations, there are {x_wins} X's wins, {o_wins} O's wins, and {ties} ties match.")
