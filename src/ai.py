import copy
from tic_tac_toe import TicTacToe

tictactoe = TicTacToe()


class Minimax(TicTacToe):
    def __init__(self, size=10):
        super().__init__(size)


    def evaluate_row(self, board, last_move, symbol):

        r, c = last_move
        count = 0
        whole_row = board[r]
        if c > 3:
            whole_row = whole_row[c-4:c+4]
        if c <= 3:
            whole_row = whole_row[:c+4]
        row_string = "".join(whole_row)
        if ' '+symbol*3+' ' in row_string:
            count+=1
        return count if symbol == 'o' else -count
    
            
    def evaluate_col(self, board, last_move, symbol):

        r, c = last_move
        count = 0
        whole_column = [row[c] for row in board]
        if r > 3:
            whole_column = whole_column[r-4:r+4]
        if c <= 3:
            whole_column = whole_column[:r+4]

        col_string = "".join(whole_column)
        if ' '+symbol*3+' ' in col_string:
            count+=1
        return count if symbol == 'o' else -count

    
    def evaluate_diag(self, board, last_move, symbol):
        count = 0
        diagonal = self.get_diagonal(board, last_move)
        counter_diagonal = self.get_counter_diagonal(board, last_move)
        if len(diagonal) >= 5:
            diagonal_string = "".join(diagonal)
            if ' '+symbol*3+' ' in diagonal_string:
                count+=1
        if len(counter_diagonal) >= 5:
            c_diagonal_string = "".join(counter_diagonal)
            if ' '+symbol*3+' ' in c_diagonal_string:
                count+=1

        return count if symbol == 'o' else -count
    

    def evaluate(self, board, moves, last_move, symbol):
        """
        Laskee siirron arvon, kun syvyys on 0.

        Parametrit:
        - board: pelilaudan tila
        - last_move (tuple (int, int)): viimeisin siirto

        Palauttaa:
        - parhaan siirron arvon (int)
        """
        return self.evaluate_row(board, last_move, symbol)+self.evaluate_col(board, last_move, symbol)+self.evaluate_diag(board, last_move, symbol)

    def minimax(self, board, depth, alpha, beta, moves, last_move, count, max_player):
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
        elif self.check_winner(board, 'o', last_move):
            return 1000000, last_move

        if depth == 0 or count == 100:
            if count == 100:
                return 0, last_move
            return self.evaluate(board, moves, last_move, "o"), last_move

        if max_player:
            best_value = -10000
            best_move = None

            updated_moves = moves.copy()
            for move in reversed(updated_moves):
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
                    max_player=False
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
            for move in reversed(updated_moves):
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
                    max_player=True
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


       
