import copy
from tic_tac_toe import TicTacToe

tictactoe = TicTacToe()


def evaluate(board, last_move, moves):
    """
    Laskee siirron arvon, kun syvyys on 0.

    Parametrit:
    - board: pelilaudan tila
    - last_move (tuple (int, int)): viimeisin siirto

    Palauttaa:
    - parhaan siirron arvon (int)
    """
    if tictactoe.check_winner(board, "x", last_move):
        return -100000, last_move
    if tictactoe.check_winner(board, "o", last_move):
        return 100000, last_move

    score = 0
    ai_symbol = 'o'
    empty_symbol = ' '
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == ai_symbol:
                score += 1
            elif board[i][j] == empty_symbol:
                score += 0.1
    
    return score


def max_value(board, depth, alpha, beta, moves, last_move):
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

    if tictactoe.check_winner(board, "x", last_move):
        return -100000, last_move

    if depth == 0:
        return evaluate(board, last_move, moves), last_move

    best_value = -10000
    best_move = None

    updated_moves = moves.copy()
    for move in reversed(updated_moves):
        row, col = move

        board[row][col] = "o"
        updated_moves = [m for m in moves if m != move]
        updated_moves = tictactoe.update_possible_moves(board, move, updated_moves)

        value, _ = min_value(
            board, depth - 1, alpha, beta, updated_moves, last_move=(row, col)
        )

        board[row][col] = " "

        if value > best_value:
            best_value = value
            best_move = move



        if best_value >= beta:

            break
        alpha = max(alpha, best_value)

    return best_value, best_move


def min_value(board, depth, alpha, beta, moves, last_move):
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

    if tictactoe.check_winner(board, "o", last_move):
        return 100000, last_move

    if depth == 0:
        return evaluate(board, last_move, moves), last_move

    best_value = 10000
    best_move = None

    updated_moves = moves.copy()
    for move in reversed(updated_moves):
        row, col = move

        board[row][col] = "x"
        updated_moves = [m for m in moves if m != move]

        updated_moves = tictactoe.update_possible_moves(board, move, updated_moves)
        value, _ = max_value(
            board, depth - 1, alpha, beta, updated_moves, last_move=(row, col)
        )

        board[row][col] = " "

        if value < best_value:
            best_value = value
            best_move = move

        if best_value <= alpha:
            break

        beta = min(beta, best_value)

    return best_value, best_move
