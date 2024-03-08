from heuristic import Heuristic

class Minimax:
    def __init__(self, size=20):
        self.possible_moves = []
        self.last_move = None
        self.size = size

    def update_board_state(self, last_move, board):
        """
        Päivittää pelilaudan tilan minimaxia varten.

        Parametrit:
        - viimeinen siirto (int)
        - pelilaudan tila list: (str)

        """
        self.last_move = last_move
        row, col = last_move
        if last_move in self.possible_moves:
            self.possible_moves.remove(last_move)
        self.possible_moves = self.update_possible_moves(
            board, (row, col), possible_moves=self.possible_moves
        )

    def get_best_move(self, board, turn):
        """
        Minimaxia kutsuva funktio

        Parametrit:
        - pelilaudan tila list: (str)
        - count (int): kertoo, monta vuoroa on pelattu

        Palauttaa:
        - parhaan siirron (tuple)


        """
        moves = self.possible_moves
        last_move = self.last_move

        _, move = self.minimax(
            board,
            depth=5,
            alpha=-10000,
            beta=10000,
            moves=moves,
            last_move=last_move,
            turn=turn,
            max_player=True,
        )
        return move

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
        Käyttää apuna alla olevia funktioita, jotka tarkastaa
        rivit, diagonaalit ja sarakkeet.

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
        move_index = None
        r, c = row, col
        while r >= 0 and c >= 0:
            diagonal.append(board[r][c])
            r -= 1
            c -= 1
        diagonal.reverse()
        move_index = len(diagonal) - 1
        r, c = row + 1, col + 1
        while r < height and c < width:
            diagonal.append(board[r][c])
            r += 1
            c += 1
        return diagonal, move_index

    def get_counter_diagonal(self, board, move):
        row, col = move
        move_index = None
        height, width = len(board), len(board[0])
        counter_diagonal = []
        r, c = row, col
        while r >= 0 and c < width:
            counter_diagonal.append(board[r][c])
            r -= 1
            c += 1
        counter_diagonal.reverse()
        move_index = len(counter_diagonal) - 1
        r, c = row + 1, col - 1
        while r < height and c >= 0:
            counter_diagonal.append(board[r][c])
            r += 1
            c -= 1

        return counter_diagonal, move_index

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
        diagonal, _ = self.get_diagonal(board, last_move)
        counter_diagonal, _ = self.get_counter_diagonal(board, last_move)
        diagonal_string = "".join(diagonal) + " " + "".join(counter_diagonal)
        if symbol * 5 in diagonal_string:
            return True
        return False

    def evaluate(self, board, last_move, symbol):
        """
        Laskee siirron arvon, kun syvyys on 0.

        Parametrit:
        - board: pelilaudan tila
        - last_move (tuple (int, int)): viimeisin siirto

        Palauttaa:
        - parhaan siirron arvon (int)
        """
        heuristic = Heuristic(minimax=Minimax())
        return (
            heuristic.evaluate_row(board, last_move, symbol)
            + heuristic.evaluate_col(board, last_move, symbol)
            + heuristic.evaluate_diag(board, last_move, symbol)
            + heuristic.evaluate_c_diag(board, last_move, symbol)
        )

    def minimax(self, board, depth, alpha, beta, moves, last_move, turn, max_player):
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

        if depth == 0 or turn == self.size * self.size:
            if turn == self.size * self.size:
                return 0, last_move
            return self.evaluate(board, last_move, "o"), last_move

        best_move = None

        if max_player:
            best_value = -10000
            updated_moves = moves.copy()
            for move in updated_moves:
                row, col = move

                board[row][col] = "o"

                turn += 1
                updated_moves = [m for m in moves if m != move]
                updated_moves = self.update_possible_moves(board, move, updated_moves)

                value, _ = self.minimax(
                    board,
                    depth - 1,
                    alpha,
                    beta,
                    updated_moves,
                    last_move=(row, col),
                    turn=turn,
                    max_player=False,
                )

                board[row][col] = " "
                turn -= 1
                alpha = max(alpha, best_value)

                if value > best_value:
                    best_value = value
                    best_move = move

                if beta <= alpha:
                    break

            return best_value, best_move

        best_value = 10000
        updated_moves = moves.copy()
        for move in updated_moves:
            row, col = move
            board[row][col] = "x"
            turn += 1
            updated_moves = [m for m in moves if m != move]
            updated_moves = self.update_possible_moves(board, move, updated_moves)
            value, _ = self.minimax(
                board,
                depth - 1,
                alpha,
                beta,
                updated_moves,
                last_move=(row, col),
                turn=turn,
                max_player=True,
            )
            board[row][col] = " "
            turn -= 1
            beta = min(beta, best_value)
            if value < best_value:
                best_value = value
                best_move = move
            if beta <= alpha:
                break
        return best_value, best_move
