class TicTacToe:
    def __init__(self, size = 10):
        self.board = [[" " for _ in range(size)] for _ in range(size)]
        self.current_player = "x"
        self.last_move = None
        self.possible_moves = []
        self.neighbors = self.generate_neighbors()

    def display_board(self):
        for row in self.board:
            print(row)

    def generate_neighbors(self):
        """
        Listaa jokaiselle ruudulle korkeintaan 
        kahden ruudun päässä olevat ruudut laudalla.

        Palauttaa:
        - neighbors (dict): dictionary, jonka avaimet ovat ruutuja,
        ja arvot lähimpiä ruutuja.
        """
        neighbors = {}
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                neighbors[(i, j)] = {
                    (x, y)
                    for x in range(i - 2, i + 3)
                    for y in range(j - 2, j + 3)
                    if 0 <= x < len(self.board)
                    and 0 <= y < len(self.board[0])
                    and (x, y) != (i, j)
                }
        return neighbors

    def update_possible_moves(self, board, last_move, possible_moves):
        """
        Päivittää seuraavat mahdolliset siirrot ruudukossa.

        Parametrit:
        - board (list): pelilauta
        - last_move (tuple: int, int): viimeisin siirto
        - possible moves (list: tuple): päivitettävä siirtolista

        Palauttaa:
        - päivitetyn siirtolistan
        """
        most_likely_moves = set()
        neighbors = self.neighbors
        for cell in neighbors[last_move]:
            row, col = cell
            if board[row][col] == " ":
                if cell in possible_moves:
                    possible_moves.remove(cell)
                    most_likely_moves.add(cell)
                elif cell not in possible_moves:
                    possible_moves.append(cell)

        possible_moves = possible_moves + list(most_likely_moves)
        for move in possible_moves:
            row, col = move
            if board[row][col] != " ":
                possible_moves.remove(move)

        return possible_moves


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

        self.possible_moves = self.update_possible_moves(
            self.board, (row, col), possible_moves=self.possible_moves
        )

        return True

    def check_winner(self, board, symbol, last_move):
        """
        Tarkistaa, onko syötteenä annettu symboli voittaja
        syötteenä annetun laudan tilassa.

        Parametrit:
        - board (list): pelilaudan tila
        - symbol (str): pelaajan symboli ('o' tai 'x')
        - last_move (tuple: int, int): viimeisen siirron koordinaatit

        Palauttaa:
        - True, jos kyseinen symboli on voittaja
        - False, jos kyseinen symboli ei ole voittaja
        """
        return (
            self.check_row(board, symbol, last_move)
            or self.check_column(board, symbol, last_move)
            or self.check_diagonal(board, symbol, last_move)
        )

    def get_diagonal(self, board, move):
        row, col = move
        height, width = len(board), len(board[0])
        diagonal = []

        r, c = row, col
        while r >= 0 and c >= 0:
            diagonal.append(board[r][c])
            r -= 1
            c -= 1

        diagonal.reverse()

        r, c = row + 1, col + 1
        while r < height and c < width:
            diagonal.append(board[r][c])
            r += 1
            c += 1

        return diagonal

    def get_counter_diagonal(self, board, move):
        row, col = move
        height, width = len(board), len(board[0])
        counter_diagonal = []

        r, c = row, col
        while r >= 0 and c < width:
            counter_diagonal.append(board[r][c])
            r -= 1
            c += 1

        counter_diagonal.reverse()

        r, c = row + 1, col - 1
        while r < height and c >= 0:
            counter_diagonal.append(board[r][c])
            r += 1
            c -= 1

        return counter_diagonal

    def check_column(self, board, symbol, move):
        _, c = move
        column = [row[c] for row in board]
        column_string = "".join(column) + "".join(column)
        if symbol * 5 in column_string:
            return True

    def check_row(self, board, symbol, move):
        r, _ = move
        row = board[r]
        row_string = "".join(row) + "".join(row)
        if symbol * 5 in row_string:
            return True

    def check_diagonal(self, board, symbol, last_move):
        diagonal = self.get_diagonal(board, last_move)
        counter_diagonal = self.get_counter_diagonal(board, last_move)
        diagonal_string = "".join(diagonal) + "".join(counter_diagonal)
        if symbol * 5 in diagonal_string:
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
