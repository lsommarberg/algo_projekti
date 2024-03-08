from board import Board
from ai import Minimax


class TicTacToeGame:
    def __init__(self):
        self.board = Board()
        self.minimax = Minimax()

    def start(self):
        while True:
            self.board.print_board()
            current_player = self.board.get_current_player()

            if current_player == "x":
                self.human_move()
            else:
                self.ai_move()

            if self.board.is_game_over(self.minimax.last_move):
                self.board.print_board()
                print("Game Over")
                break

    def human_move(self):
        """
        Ottaa ihmispelaajan antaman siirron rivin ja sarakkeen.

        Tarkistaa siirron laillisuuden ja tekee siirron tai antaa virheilmoituksen.
        """
        valid_move = False
        while not valid_move:
            try:
                row = int(input("Enter row (1-20): ")) - 1
                col = int(input("Enter column (1-20): ")) - 1
                if row in range(self.board.size) and col in range(self.board.size):
                    valid_move = self.board.make_move(row, col, "x")
                    if valid_move:
                        self.minimax.update_board_state((row, col), self.board.board)
                        self.board.current_player = "o"
                        valid_move = True
                    else:
                        print("Cell is already occupied. Please choose another cell.")
                else:
                    print("Invalid move, please enter numbers between 1 and 20.")
            except ValueError:
                print("Invalid input. Please enter numbers.")

    def ai_move(self):
        """
        Hakee tekoälyn siirron.

        Päivittää pelilaudan siirron jälkeen.
        """
        row, col = self.minimax.get_best_move(self.board.board, self.board.turn)
        valid_move = self.board.make_move(row, col, "o")
        if valid_move:
            self.minimax.update_board_state((row, col), self.board.board)
            self.board.current_player = "x"
