import copy
from tic_tac_toe import TicTacToe

tictactoe = TicTacToe()

class Minimax(TicTacToe):
    def __init__(self, size=10):
        super().__init__(size)

    
    def evaluate(self, board, moves, last_move, symbol):
        """
        Laskee siirron arvon, kun syvyys on 0.

        Parametrit:
        - board: pelilaudan tila
        - last_move (tuple (int, int)): viimeisin siirto

        Palauttaa:
        - parhaan siirron arvon (int)
        """
        score = 0
        ai_symbol = symbol
        empty_symbol = ' '
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ai_symbol:
                    score += 1
                elif board[i][j] == empty_symbol:
                    score += 0.1
        
        return score

    def max_value(self, board, depth, alpha, beta, moves, last_move, counter):
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
            return -100000, last_move

        if counter == 100:
            return 0, last_move
        
        if depth == 0:
            return self.evaluate(board, moves, last_move, 'o'), last_move

        best_value = -10000
        best_move = None

        updated_moves = moves.copy()
        for move in reversed(updated_moves):
            row, col = move

            board[row][col] = "o"
            counter += 1
            updated_moves = [m for m in moves if m != move]
            updated_moves = self.update_possible_moves(board, move, updated_moves)

            value, _ = self.min_value(
                board, depth - 1, alpha, beta, updated_moves, last_move=(row, col), counter=counter
            )

            board[row][col] = " "
            counter -= 1
            if value > best_value:
                best_value = value
                best_move = move

            if best_value >= beta:
                break

            alpha = max(alpha, best_value)

        return best_value, best_move


    def min_value(self, board, depth, alpha, beta, moves, last_move, counter):
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
            return 100000, last_move

        if counter == 100:
            return 0, last_move
        
        if depth == 0:
            return self.evaluate(board, moves, last_move, 'x'), last_move

        best_value = 10000
        best_move = None

        updated_moves = moves.copy()
        for move in reversed(updated_moves):
            row, col = move

            board[row][col] = "x"
            counter += 1
            updated_moves = [m for m in moves if m != move]

            updated_moves = self.update_possible_moves(board, move, updated_moves)
            value, _ = self.max_value(
                board, depth - 1, alpha, beta, updated_moves, last_move=(row, col), counter=counter
            )

            board[row][col] = " "
            counter -= 1
            if value < best_value:
                best_value = value
                best_move = move

            if best_value <= alpha:
                break

            beta = min(beta, best_value)

        return best_value, best_move
