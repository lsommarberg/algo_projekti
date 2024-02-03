import copy
from tic_tac_toe import TicTacToe


class State(TicTacToe):
    def __init__(self, state, player, move):
        """
        Tallentaa pelilaudan tilan annetussa hetkessä luokkaobjektiksi

        Parametrit:
        - pelilauta (list): 2D lista laudan tilasta
        - pelaaja (str): 'o' tai 'x', seuraavan siirron perusteella
        - move (tuple(int, int)): viimeisin siirto
        """
        super().__init__()
        self.state = state
        self.player = player
        self.move = move

    def children(self):
        """
        Laskee seuraavat mahdolliset siirrot kyseisessä tilassa,
        ja lisää ne listaan

        Palauttaa:
        - listan seuraavista mahdollisista siirroista State objekteina
        """

        current_board = self.state

        child_nodes = []

        for row in range(len(current_board)):
            for col in range(len(current_board)):
                if current_board[row][col] == " ":
                    new_board = copy.deepcopy(current_board)

                    new_board[row][col] = self.player
                    next_player = "x" if self.player == "o" else "o"

                    child_nodes.append(State(new_board, next_player, (row, col)))

        return child_nodes

    def is_terminal_state(self):
        """
        Tarkistaa, onko kyseisen objektin lauta voittotilassa tai tasapelissä

        Palauttaa:
        - True, jos voittaja löytyy, tai kyseessä on tasapeli
        - False, jos peli vielä jatkuu
        """
        if self.check_draw(self.state):
            return True

        if self.check_winner(self.state, symbol="x") or self.check_winner(
            self.state, symbol="o"
        ):
            return True

        return False


class TicTacToeAI(TicTacToe):
    def __init__(self):
        super().__init__()

    def evaluate(self, node):
        """
        Laskee pisteet kyseisessä pelilaudan tilassa

        Parametrit:
        - node State(): sisältää State objektin


        Palauttaa:
        - minimax arvon (int)
        """
        board_state = node.state
        opponent_wins = self.check_winner(board_state, symbol="x")
        ai_wins = self.check_winner(board_state, symbol="o")
        if opponent_wins:
            return -10
        if ai_wins:
            return 10

        return 0

    def max_value(self, node, depth, alpha, beta):
        """
        Maksimoiva pelaaja

        Parametrit:
        - node State(): sisältää State objektin
        - depth (int): syvyys, jossa arvo lasketaan
        - alpha (int): alpha beta karsinnan alpha arvo
        - beta (int): alpha beta karsinnan beta arvo

        Palauttaa:
        - maksimiarvon (int)
        """

        if node.is_terminal_state() or depth == 0:
            return self.evaluate(node)
        best_value = -10000
        for child in node.children():
            value = self.min_value(child, depth - 1, alpha, beta)
            best_value = max(value, best_value)
            alpha = max(alpha, best_value)
            if best_value >= beta:
                break
        return best_value

    def min_value(self, node, depth, alpha, beta):
        """
        Minimoiva pelaaja

        Parametrit:
        - node State(): sisältää State objektin
        - depth (int): syvyys, jossa arvo lasketaan
        - alpha (int): alpha beta karsinnan alpha arvo
        - beta (int): alpha beta karsinnan beta arvo

        Palauttaa:
        - minimiarvon (int)
        """
        if node.is_terminal_state() or depth == 0:
            return self.evaluate(node)
        best_value = 10000
        for child in node.children():
            value = self.max_value(child, depth - 1, alpha, beta)
            best_value = min(value, best_value)
            beta = min(beta, best_value)
            if best_value <= alpha:
                break
        return best_value

    def ai_make_move(self, board):
        """
        Laskee rekursiivisesti parhaan mahdollisen
        siirron tulevien siirtojen perusteella.

        Parametrit:
        - board (list): pelilaudan tila

        Palauttaa:
        - best_move (int): paras siirto
        """
        state = State(board, "o", self.last_move)
        best_move = state.move
        best_value = -1000
        for child in state.children():
            value = self.max_value(child, depth=3, alpha=-10000, beta=10000)
            if value > best_value:
                best_value = value
                best_move = child.move

        return best_move
