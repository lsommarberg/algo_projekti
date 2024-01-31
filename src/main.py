from ai import TicTacToeAI


def main():
    game = TicTacToeAI()

    while True:
        game.display_board()


        if game.current_player == "x":
            row = int(input(f"Player {game.current_player}, enter the row (0-2): "))
            col = int(input(f"Player {game.current_player}, enter the column (0-2): "))

            if game.make_move(row, col):
                game.last_move = row, col
                game.switch_player()
            else:
                print("invalid move, try again.")
        else:
            ai_row, ai_col = game.ai_make_move(game.board)

            if game.make_move(ai_row, ai_col):
                game.switch_player()
                print("\n")
            else:
                print("invalid move, try again.")

        if game.check_winner(game.board, "x"):
            game.display_board()
            print("x wins")
            break

        if game.check_winner(game.board, "o"):
            game.display_board()
            print("o wins")
            break

        if game.check_draw(game.board):
            game.display_board()
            print("draw")
            break


if __name__ == "__main__":
    main()
