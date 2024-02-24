class Minimax:
    def __init__(self, size=20):
        self.possible_moves = []
        self.last_move = None
        self.size = size

    def update_board_state(self, last_move, board):
        self.last_move = last_move
        row, col = last_move
        if last_move in self.possible_moves:
            self.possible_moves.remove(last_move)
        self.possible_moves = self.update_possible_moves(
            board, (row, col), possible_moves=self.possible_moves
        )

    def get_best_move(self, board, count):
        moves = self.possible_moves
        last_move = self.last_move
        _, (ai_row, ai_col) = self.minimax(
            board,
            depth=5,
            alpha=-10000,
            beta=10000,
            moves=moves,
            last_move=last_move,
            count=count,
            max_player=True,
        )
        return ai_row, ai_col

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
        most_likely_moves = []
        updated_moves = []
        row, col = last_move
        for i in range(max(0, row - 2), min(len(board), row + 3)):
            for j in range(max(0, col - 2), min(len(board[0]), col + 3)):
                if board[i][j] == " ":
                    if (i, j) in possible_moves:
                        most_likely_moves.append((i, j))
                        possible_moves = [m for m in possible_moves if m != (i, j)]
                    else:
                        updated_moves.append((i, j))

        return most_likely_moves + possible_moves + updated_moves

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
        column_string = "".join(column)
        if symbol * 5 in column_string:
            return True
        return False

    def check_row(self, board, symbol, move):
        r, _ = move
        row = board[r]
        row_string = "".join(row)
        if symbol * 5 in row_string:
            return True
        return False

    def check_diagonal(self, board, symbol, last_move):
        diagonal = self.get_diagonal(board, last_move)
        counter_diagonal = self.get_counter_diagonal(board, last_move)
        diagonal_string = "".join(diagonal) + " " + "".join(counter_diagonal)
        if symbol * 5 in diagonal_string:
            return True
        return False

    def evaluate_row(self, board, last_move, symbol):
        score = 0
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

        all_cells = cells_to_left + cells_to_right
        row_string = "".join(all_cells)
        if " " + symbol * 3 + " " in row_string:
            score += 5

        return score if symbol == "o" else -score

    def evaluate_col(self, board, last_move, symbol):
        r, c = last_move
        score = 0
        whole_column = [row[c] for row in board]
        cells_to_right = []

        for i in range(0, 5):
            if r + i < len(whole_column):
                cells_to_right.append(whole_column[r + i])
            else:
                break

        cells_to_left = []
        for i in range(1, 5):
            if r - i >= 0:
                cells_to_left.append(whole_column[r - i])
            else:
                break

        all_cells = cells_to_left + cells_to_right
        col_string = "".join(all_cells)
        if " " + symbol * 3 + " " in col_string:
            score += 5

        return score if symbol == "o" else -score

    def evaluate_diag(self, board, last_move, symbol):
        score = 0
        r, _ = last_move
        diagonal = self.get_diagonal(board, last_move)

        if len(diagonal) >= 5:
            cells_to_right = []

            for i in range(0, 5):
                if r + i < len(diagonal):
                    cells_to_right.append(diagonal[r + i])
                else:
                    break

            cells_to_left = []
            for i in range(1, 5):
                if r - i >= 0 and r <= len(diagonal):
                    cells_to_left.append(diagonal[r - i])
                else:
                    break

            all_cells = cells_to_left + cells_to_right
            diagonal_string = "".join(all_cells)
            if " " + symbol * 3 + " " in diagonal_string:
                score += 5

        return score if symbol == "o" else -score

    def evaluate_c_diag(self, board, last_move, symbol):
        score = 0
        r, _ = last_move
        counter_diagonal = self.get_counter_diagonal(board, last_move)
        cells_to_right = []
        if len(counter_diagonal) >= 5:
            for i in range(0, 5):
                if r + i < len(counter_diagonal):
                    cells_to_right.append(counter_diagonal[r + i])
                else:
                    break

            cells_to_left = []
            for i in range(1, 5):
                if r - i >= 0 and r - i < len(counter_diagonal):
                    cells_to_left.append(counter_diagonal[r - i])
                else:
                    break

            all_cells = cells_to_left + cells_to_right
            c_diagonal_string = "".join(all_cells)
            if " " + symbol * 3 + " " in c_diagonal_string:
                score += 5

        return score if symbol == "o" else -score

    def evaluate(self, board, last_move, symbol):
        """
        Laskee siirron arvon, kun syvyys on 0.

        Parametrit:
        - board: pelilaudan tila
        - last_move (tuple (int, int)): viimeisin siirto

        Palauttaa:
        - parhaan siirron arvon (int)
        """
        return (
            self.evaluate_row(board, last_move, symbol)
            + self.evaluate_col(board, last_move, symbol)
            + self.evaluate_diag(board, last_move, symbol)
            + self.evaluate_c_diag(board, last_move, symbol)
        )

    def minimax(self, board, depth, alpha, beta, moves, last_move, count, max_player):
        """
        Minimax

        Parametrit:
        - board: pelilaudan tila
        - depth (int): syvyys, jossa arvo lasketaan
        - alpha (int): alpha beta karsinnan alpha arvo
        - beta (int): alpha beta karsinnan beta arvo
        - moves (list: tuple): seuraavien siirtojen lista
        - last_move (tuple (int, int)): viimeisin siirto
        - count (int): pelattujen vuorojen määrä
        - max_player (bool): maksimoiva pelaaja

        Palauttaa:
        - maksimiarvon (int)
        - parhaan siirron (tuple)
        """

        if self.check_winner(board, "o", last_move):
            return 1000000, last_move
        if self.check_winner(board, "x", last_move):
            return -1000000, last_move

        if depth == 0 or count == 200:
            if count == 200:
                return 0, last_move
            player = "o" if max_player else "x"
            return self.evaluate(board, last_move, player), last_move

        if max_player:
            best_value = -10000
            best_move = None

            updated_moves = moves.copy()
            for move in updated_moves:
                row, col = move

                board[row][col] = "o"

                count += 1
                updated_moves = [m for m in moves if m != move]
                updated_moves = self.update_possible_moves(board, move, updated_moves)

                value, _ = self.minimax(
                    board,
                    depth - 1,
                    alpha,
                    beta,
                    updated_moves,
                    last_move=(row, col),
                    count=count,
                    max_player=False,
                )

                board[row][col] = " "
                count -= 1
                if value > best_value:
                    best_value = value
                    best_move = move

                if best_value >= beta:
                    break

                alpha = max(alpha, best_value)

            return best_value, best_move

        else:
            best_value = 10000
            best_move = None
            updated_moves = moves.copy()
            for move in updated_moves:
                row, col = move
                board[row][col] = "x"
                count += 1
                updated_moves = [m for m in moves if m != move]
                updated_moves = self.update_possible_moves(board, move, updated_moves)
                value, _ = self.minimax(
                    board,
                    depth - 1,
                    alpha,
                    beta,
                    updated_moves,
                    last_move=(row, col),
                    count=count,
                    max_player=True,
                )
                board[row][col] = " "
                count -= 1
                if value < best_value:
                    best_value = value
                    best_move = move

                if best_value <= alpha:
                    break

                beta = min(beta, best_value)

            return best_value, best_move
