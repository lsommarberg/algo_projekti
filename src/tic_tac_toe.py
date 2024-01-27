class TicTacToe:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.current_player = "x"

    def display_board(self):
        for row in self.board:
            print(row)

    def make_move(self, row, col):
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
        self.board[row][col] = self.current_player
        return True

    def check_winner(self, board, symbol):
        """
        Tarkistaa, onko syötteenä annettu symboli voittaja
        syötteenä annetun laudan tilassa.

        Parametrit:
        - board (list): pelilaudan tila
        - symbol (str): pelaajan symboli ('o' tai 'x')

        Palauttaa:
        - True, jos kyseinen symboli on voittaja
        - False, jos kyseinen symboli ei ole voittaja
        """
        items = []
        # rows
        for item in board:
            items.append(item)

        # columns
        for index in range(len(board[0])):
            col = [ele[index] for ele in board]
            items.append(col)

        # diagonals
        diag = [row[i] for i, row in enumerate(board)]
        c_diag = [row[~i] for i, row in enumerate(board)]
        items.append(diag)
        items.append(c_diag)

        items_as_strings = ["".join(inner_list) for inner_list in items]

        for string in items_as_strings:
            if string == symbol * 3:
                return True
        return False

    def check_draw(self, board):
        """
        Tarkistaa, onko syötteenä annettu lauta tasapelissä.

        Parametrit:
        - board (list): pelilaudan tila

        Palauttaa:
        - True, jos kyseessä on tasapeli
        - False, jos kyseessä ei ole tasapeli
        """
        board_values = [cell for row in board for cell in row]
        board_values_as_set = set(board_values)
        return " " not in board_values_as_set

    def switch_player(self):
        self.current_player = "o" if self.current_player == "x" else "x"

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

        # row, col for indeces
        if self.board[row][col] == " ":
            return True
        return False
