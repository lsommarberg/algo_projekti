import copy
from tic_tac_toe import TicTacToe

tictactoe = TicTacToe()


class Minimax(TicTacToe):
    def __init__(self, size=10):
        super().__init__(size)
        self.neighbors = self.generate_3x3_neighbors(self.board)

    def generate_3x3_neighbors(self, board):
        """
        Hakee 3x3 ruudukon kaikille laudan ruuduille
        Palauttaa:
        - listan ruuduista 3x3 säteellä
        """
        neighbors = {}
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                min_x = max(0, i - 1)
                max_x = min(rows - 1, i + 1)
                min_y = max(0, j - 1)
                max_y = min(cols - 1, j + 1)
                neighbor_cells = {
                    (x, y)
                    for x in range(min_x, max_x + 1)
                    for y in range(min_y, max_y + 1)
                }
                neighbors[(i, j)] = neighbor_cells
        return neighbors

    def get_3x3_neighbors(self, last_move):
        """
        Hakee 3x3 ruudukon annetun siirron ympärillä

        Parametrit:
        - last_move (tuple (int, int)): viimeisin siirto

        Palauttaa:
        - listan ruuduista 3x3 säteellä
        """
        neighbors = self.neighbors
        return neighbors[last_move]

    def evaluate_neighbors(self, board, last_move, symbol):
        """
        Hakee eri kuvioita ja pisteyttää ne.

        Parametrit:
        - board (list): pelilaudan tila
        - last_move (tuple (int, int)): viimeisin siirto
        - symbol: 'o' tai 'x'

        Palauttaa:
        - pisteet annetulle siirrolle
        """
        scores = 0
        patterns = {
            symbol * 4: 10,
            symbol * 3: 5,
        }
        neighbors = self.get_3x3_neighbors(last_move)
        row, col = last_move
        for pattern, score in patterns.items():
            for i, j in neighbors:
                if i == row:
                    if 0 <= j + len(pattern) - 1 < len(board[0]):
                        row_str = "".join(board[i][j : j + len(pattern)])
                        if row_str == pattern:
                            scores += score if symbol == "o" else scores - score
                    if 0 <= j - len(pattern) + 1 < len(board[0]):
                        row_str = "".join(board[i][j - len(pattern) + 1 : j + 1])
                        if row_str == pattern:
                            scores += score if symbol == "o" else scores - score

            for i, j in neighbors:
                if j == col:
                    if 0 <= i + len(pattern) - 1 < len(board):
                        col_str = "".join(
                            board[k][j] for k in range(i, i + len(pattern))
                        )
                        if col_str == pattern:
                            scores += score if symbol == "o" else scores - score

                    if 0 <= i - len(pattern) + 1 < len(board):
                        col_str = "".join(
                            board[k][j] for k in range(i - len(pattern) + 1, i + 1)
                        )
                        if col_str == pattern:
                            scores += score if symbol == "o" else scores - score

            for i, j in neighbors:
                if row - col == i - j:
                    if 0 <= row + len(pattern) - 1 < len(board) and 0 <= col + len(
                        pattern
                    ) - 1 < len(board[0]):
                        diag_str = "".join(
                            board[row + k][col + k] for k in range(len(pattern))
                        )
                        if diag_str == pattern:
                            scores += score if symbol == "o" else scores - score

                    if 0 <= row - len(pattern) + 1 < len(board) and 0 <= col - len(
                        pattern
                    ) + 1 < len(board[0]):
                        diag_str = "".join(
                            board[row - k][col - k] for k in range(len(pattern))
                        )
                        if diag_str == pattern:
                            scores += score if symbol == "o" else scores - score

                if row + col == i + j:
                    if 0 <= row + len(pattern) - 1 < len(board) and 0 <= col - len(
                        pattern
                    ) + 1 < len(board[0]):
                        diag_str = "".join(
                            board[row + k][col - k] for k in range(len(pattern))
                        )
                        if diag_str == pattern:
                            scores += score if symbol == "o" else scores - score

                    if 0 <= row - len(pattern) + 1 < len(board) and 0 <= col + len(
                        pattern
                    ) - 1 < len(board[0]):
                        diag_str = "".join(
                            board[row - k][col + k] for k in range(len(pattern))
                        )
                        if diag_str == pattern:
                            scores += score if symbol == "o" else scores - score
        return scores

    def evaluate(self, board, moves, last_move, symbol):
        """
        Laskee siirron arvon, kun syvyys on 0.

        Parametrit:
        - board: pelilaudan tila
        - last_move (tuple (int, int)): viimeisin siirto

        Palauttaa:
        - parhaan siirron arvon (int)
        """
        return self.evaluate_neighbors(board, last_move, symbol)

    def max_value(self, board, depth, alpha, beta, moves, last_move, count):
        """
        Maksimoiva pelaaja

        Parametrit:
        - board: pelilaudan tila
        - depth (int): syvyys, jossa arvo lasketaan
        - alpha (int): alpha beta karsinnan alpha arvo
        - beta (int): alpha beta karsinnan beta arvo
        - moves (list: tuple): seuraavien siirtojen lista
        - last_move (tuple (int, int)): viimeisin siirto

        Palauttaa:
        - maksimiarvon (int)
        - parhaan siirron (tuple)
        """

        if self.check_winner(board, "x", last_move):
            return -1000000, last_move

        if depth == 0 or count == 100:
            if count == 100:
                return 0, last_move
            return self.evaluate(board, moves, last_move, "o"), last_move

        best_value = -10000
        best_move = None

        updated_moves = moves.copy()
        for move in reversed(updated_moves):
            row, col = move

            board[row][col] = "o"
            count += 1
            updated_moves = [m for m in moves if m != move]
            updated_moves = self.update_possible_moves(board, move, updated_moves)

            value, _ = self.min_value(
                board,
                depth - 1,
                alpha,
                beta,
                updated_moves,
                last_move=(row, col),
                count=count,
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

    def min_value(self, board, depth, alpha, beta, moves, last_move, count):
        """
        Minimoiva pelaaja

        Parametrit:
        - board: pelilaudan tila
        - depth (int): syvyys, jossa arvo lasketaan
        - alpha (int): alpha beta karsinnan alpha arvo
        - beta (int): alpha beta karsinnan beta arvo
        - moves (list: tuple): seuraavien siirtojen lista
        - last_move (tuple (int, int)): viimeisin siirto

        Palauttaa:
        - minimiarvon (int)
        - parhaan siirron (tuple)
        """

        if self.check_winner(board, "o", last_move):
            return 1000000, last_move

        if depth == 0 or count == 100:
            if count == 100:
                return 0, last_move
            return self.evaluate(board, moves, last_move, "x"), last_move

        best_value = 10000
        best_move = None

        updated_moves = moves.copy()
        for move in reversed(updated_moves):
            row, col = move

            board[row][col] = "x"
            count += 1
            updated_moves = [m for m in moves if m != move]

            updated_moves = self.update_possible_moves(board, move, updated_moves)
            value, _ = self.max_value(
                board,
                depth - 1,
                alpha,
                beta,
                updated_moves,
                last_move=(row, col),
                count=count,
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
