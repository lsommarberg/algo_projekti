from tic_tac_toe import TicTacToe


class TicTacToeAI(TicTacToe):
    def __init__(self):
        super().__init__()

    def evaluate(self, node):
        board_state = node
        opponent_wins = self.check_winner(board_state, symbol="x")
        ai_wins = self.check_winner(board_state, symbol="o")
        if opponent_wins:
            return -10
        if ai_wins:
            return 10
        return 0

    def children(self, node):
        """
        Laskee seuraavat mahdolliset siirrot kyseisessä solmussa,
        ja lisää ne listaan

        Parametrit:
        - node (tuple: ((str), (list)): sisältää tämänhetkisen pelaajan symbolin ja
        pelilaudan tilan

        Palauttaa:
        - listan seuraavista mahdollisista siirroista
        """
        current_player_symbol = node[0]

        current_board = node[1]

        child_nodes = []

        for row in range(3):
            for col in range(3):
                if current_board[row][col] == " ":
                    new_board = [row.copy() for row in current_board]

                    new_board[row][col] = current_player_symbol

                    next_player_symbol = "x" if current_player_symbol == "o" else "o"

                    child_nodes.append(((row, col), (next_player_symbol, new_board)))

        return child_nodes

    def is_terminal_state(self, board):
        """
        Tarkistaa, onko syötteenä annettu lauta tasapelissä,
        tai onko toinen pelaajista voittanut.

        Parametrit:
        - board (list): pelilaudan tila

        Palauttaa:
        - True, jos voittaja löytyy, tai kyseessä on tasapeli
        - False, jos peli vielä jatkuu
        """
        if self.check_winner(board, "x") or self.check_winner(board, "o"):
            return True

        if self.check_draw(board):
            return True

        return False

    def minimax(self, node, depth, max_player):
        """
        Laskee rekursiivisesti parhaan mahdollisen
        siirron tulevien siirtojen perusteella.

        Parametrit:
        - node (tuple: ((str), (list)): sisältää tämänhetkisen pelaajan symbolin ja
        pelilaudan tilan
        - depth (int): syvyys, jossa seuraavia siirtoja lasketaan
        - max_player (bool):

        Palauttaa:
        - Parhaan siirron ja minimax-arvon
        """

        if depth == 0 or self.is_terminal_state(node[-1]):
            return self.evaluate(node[-1]), None

        if max_player:
            best_value = float("-inf")
            best_move = None
            for move, child in self.children(node):
                value, _ = self.minimax(child, depth - 1, False)
                if value > best_value:
                    best_value = value
                    best_move = move
            return best_value, best_move
        else:
            best_value = float("inf")
            best_move = None
            for move, child in self.children(node):
                value, _ = self.minimax(child, depth - 1, True)
                if value < best_value:
                    best_value = value
                    best_move = move
            return best_value, best_move

    def ai_make_move(self, board):
        _, best_move = self.minimax(
            (self.current_player, board), depth=4, max_player=True
        )

        return best_move
