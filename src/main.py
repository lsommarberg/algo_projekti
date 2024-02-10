from tic_tac_toe import TicTacToe
from ai import max_value
import copy


def main():
    game = TicTacToe()
    counter = 0
    player = "x"
    while True:
        game.display_board()
        if player == "x":
            row = int(input(f"Player {game.current_player}, enter the row (0-2): "))
            col = int(input(f"Player {game.current_player}, enter the column (0-2): "))

            if game.make_move(row, col, "x"):
                counter += 1
                player = "o"
            else:
                print("invalid move, try again.")
        else:
            board = copy.deepcopy(game.board)
            moves = game.possible_moves
            last_move = game.last_move
            _, (ai_row, ai_col) = max_value(
                board,
                depth=5,
                alpha=-10000,
                beta=10000,
                moves=moves,
                last_move=last_move,
            )

            if game.make_move(ai_row, ai_col, "o"):
                counter += 1
                player = "x"
                print("\n")
            else:
                print("invalid move, try again.")

        if game.check_winner(game.board, "x", game.last_move):
            game.display_board()
            print("x wins")
            break

        if game.check_winner(game.board, "o", game.last_move):
            game.display_board()
            print("o wins")
            break

        if counter == 100:
            print("draw")
            break


if __name__ == "__main__":
    main()
