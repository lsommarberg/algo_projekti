class Board:
    def __init__(self, size=20):
        self.board = [[" " for _ in range(size)] for _ in range(size)]
        self.current_player = "x"
        self.turn = 0
        self.size = size

    def print_board(self):
        max_index = self.size * self.size
        cell_width = len(str(max_index))

        print("  " + " ".join(str(i + 1).rjust(cell_width) for i in range(self.size)))

        print(" ", end="")
        print("-" * (self.size * (cell_width + 1) + 2))

        for i in range(self.size):
            row = []
            for j in range(self.size):
                if self.board[i][j] == " ":
                    row.append(" " * cell_width)
                else:
                    row.append(self.board[i][j].rjust(cell_width))
            if i < 9:
                j = " "
            else:
                j = ""
            print(f"{i + 1}" + j + "|" + "|".join(row) + "|")
            print(" ", end="")
            print("-" * (self.size * (cell_width + 1) + 2))

    def is_game_over(self, last_move):
        from ai import Minimax

        minimax = Minimax()
        if minimax.check_winner(self.board, "x", last_move):
            print("x wins!")
            return True
        if minimax.check_winner(self.board, "o", last_move):
            print("o wins!")
            return True
        if self.turn == 200:
            print("draw")
        return False

    def get_current_player(self):
        return self.current_player

    def make_move(self, row, col, symbol):
        """
        Tekee siirron rivin ja sarakkeen perusteella

        Parametrit:
        - row (int): rivi
        - col (int): sarake

        Palauttaa:
        - True, jos siirto onnistui
        - False, jos siirto epäonnistui
        """
        if not self.is_valid_move(row, col):
            return False

        self.last_move = row, col
        self.board[row][col] = symbol
        self.turn += 1
        return True

    def is_valid_move(self, row, col):
        """
        Tarkistaa, onko syötteenä annettu siirto hyväksytty.

        Parametrit:
        - row (int): rivi
        - col (int): sarake

        Palauttaa:
        - True, jos ruutu on tyhjä
        - False, jos ruutu ei ole tyhjä
        """

        if self.board[row][col] == " ":
            return True
        return False
