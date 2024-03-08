class Heuristic:
    def __init__(self, minimax):
        self.minimax = minimax

    def evaluate_row(self, board, last_move, symbol):
        """
        Laskee, löytyykö rivistä kuvio, jossa on kolme symbolia,
        ja vapaa ruutu toisella puolella.
        Jos tällaista kuviota ei löydy, laskee, onko siirto blokkaava.

        Parametrit:
        - board: pelilaudan tila
        - last_move (tuple (int, int)): viimeisin siirto
        - symbol (str): pelaajan symboli

        Palauttaa:
        - pisteet (int): 50 tai 30, jos kuvio löytyy. 0, jos ei löydy
        """
        score = 0
        opponent_symbol = "x"

        r, c = last_move
        whole_row = board[r]
        cells_to_right = []
        for i in range(0, 5):
            if c + i < len(whole_row):
                cells_to_right.append(whole_row[c + i])
            else:
                break

        cells_to_left = []
        for i in range(1, 5):
            if c - i >= 0:
                cells_to_left.append(whole_row[c - i])
            else:
                break

        cells_to_left.reverse()
        all_cells = cells_to_left + cells_to_right
        row_string = "".join(all_cells)
        if " " + symbol * 3 in row_string or symbol * 3 + " " in row_string:
            score += 50
        elif (
            opponent_symbol * 3 + symbol in row_string
            or symbol + opponent_symbol * 3 in row_string
        ):
            score += 30

        return score

    def evaluate_col(self, board, last_move, symbol):
        """
        Laskee, löytyykö pystyrivistä kuvio, jossa on kolme symbolia,
        ja vapaa ruutu toisella puolella.
        Jos tällaista kuviota ei löydy, laskee, onko siirto blokkaava.

        Parametrit:
        - board: pelilaudan tila
        - last_move (tuple (int, int)): viimeisin siirto
        - symbol (str): pelaajan symboli

        Palauttaa:
        - pisteet (int): 50 tai 30, jos kuvio löytyy. 0, jos ei löydy
        """
        r, c = last_move
        opponent_symbol = "x" if symbol == "o" else "o"

        score = 0
        whole_column = [row[c] for row in board]
        cells_to_right = []

        for i in range(0, 4):
            if r + i < len(whole_column):
                cells_to_right.append(whole_column[r + i])
            else:
                break

        cells_to_left = []
        for i in range(1, 4):
            if r - i >= 0:
                cells_to_left.append(whole_column[r - i])
            else:
                break

        cells_to_left.reverse()
        all_cells = cells_to_left + cells_to_right
        col_string = "".join(all_cells)
        if " " + symbol * 3 in col_string or symbol * 3 + " " in col_string:
            score += 50
        elif (
            opponent_symbol * 3 + symbol in col_string
            or symbol + opponent_symbol * 3 in col_string
        ):
            score += 30
        return score

    def evaluate_diag(self, board, last_move, symbol):
        """
        Laskee, löytyykö vinottaisesta rivistä kuvio, jossa on kolme symbolia,
        ja vapaa ruutu toisella puolella.
        Jos tällaista kuviota ei löydy, laskee, onko siirto blokkaava.

        Parametrit:
        - board: pelilaudan tila
        - last_move (tuple (int, int)): viimeisin siirto
        - symbol (str): pelaajan symboli

        Palauttaa:
        - pisteet (int): 50 tai 30, jos kuvio löytyy. 0, jos ei löydy
        """
        opponent_symbol = "x"

        score = 0
        diagonal, move_index = self.minimax.get_diagonal(board, last_move)

        if len(diagonal) >= 5:
            cells_to_right = []

            for i in range(0, 4):
                if move_index + i < len(diagonal):
                    cells_to_right.append(diagonal[move_index + i])
                else:
                    break

            cells_to_left = []
            for i in range(1, 4):
                if move_index - i >= 0:
                    cells_to_left.append(diagonal[move_index - i])
                else:
                    break

            cells_to_left.reverse()
            all_cells = cells_to_left + cells_to_right
            diagonal_string = "".join(all_cells)
            if (
                " " + symbol * 3 in diagonal_string
                or symbol * 3 + " " in diagonal_string
            ):
                score += 50
            elif (
                opponent_symbol * 3 + symbol in diagonal_string
                or symbol + opponent_symbol * 3 in diagonal_string
            ):
                score += 30

        return score

    def evaluate_c_diag(self, board, last_move, symbol):
        """
        Laskee, löytyykö vinottaisesta rivistä kuvio, jossa on kolme symbolia,
        ja vapaa ruutu toisella puolella.
        Jos tällaista kuviota ei löydy, laskee, onko siirto blokkaava.

        Parametrit:
        - board: pelilaudan tila
        - last_move (tuple (int, int)): viimeisin siirto
        - symbol (str): pelaajan symboli

        Palauttaa:
        - pisteet (int): 50 tai 30, jos kuvio löytyy. 0, jos ei löydy
        """
        opponent_symbol = "x"
        score = 0
        counter_diagonal, move_index = self.minimax.get_counter_diagonal(
            board, last_move
        )
        cells_to_right = []
        if len(counter_diagonal) >= 5:
            for i in range(0, 4):
                if move_index + i < len(counter_diagonal):
                    cells_to_right.append(counter_diagonal[move_index + i])
                else:
                    break

            cells_to_left = []
            for i in range(1, 4):
                if move_index - i >= 0:
                    cells_to_left.append(counter_diagonal[move_index - i])
                else:
                    break
            cells_to_left.reverse()
            all_cells = cells_to_left + cells_to_right
            c_diagonal_string = "".join(all_cells)
            if (
                " " + symbol * 3 in c_diagonal_string
                or symbol * 3 + " " in c_diagonal_string
            ):
                score += 50
            elif (
                opponent_symbol * 3 + symbol in c_diagonal_string
                or symbol + opponent_symbol * 3 in c_diagonal_string
            ):
                score += 30

        return score
