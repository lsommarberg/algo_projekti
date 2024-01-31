from tic_tac_toe import TicTacToe

class State(TicTacToe):
    def __init__(self, state, player, move):
        """
        Tallentaa pelilaudan tilan annetussa hetkessä luokkaobjektiksi

        Parametrit:
        - pelilauta (list): 2D lista laudan tilasta
        - pelaaja (str): 'o' tai 'x', seuraavan siirron perusteella
        """
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

        turn = 'x' if self.player == 'x' else 'o'

        child_nodes = []

        for row in range(3):
            for col in range(3):
                if current_board[row][col] == " ":
                    new_board = [row.copy() for row in current_board]
                    
                    new_board[row][col] = turn

                    next_player_symbol = "x" if turn == "o" else "o"

                    child_nodes.append(State(new_board, next_player_symbol, (row, col)))

        return child_nodes

    def is_terminal_state(self):
        """
        Tarkistaa, onko kyseisen objektin lauta voittotilassa tai tasapelissä

        Palauttaa:
        - True, jos voittaja löytyy, tai kyseessä on tasapeli
        - False, jos peli vielä jatkuu
        """
        if self.check_winner(self.state, symbol="x") or self.check_winner(self.state, symbol="o"):
            return True

        if self.check_draw(self.state):
            return True

        return False


class TicTacToeAI(TicTacToe):
    def __init__(self):
        super().__init__()

    def evaluate(self, node, depth):
        """
        Laskee pisteet kyseisessä tilassa, jos kyseessä oli vastustajan siirto

        Parametrit:
        - node State(): sisältää State objektin
        - depth (int): syvyys, jossa seuraavia siirtoja lasketaan

        Palauttaa:
        - minimax arvon (int)
        """
        if node.player == 'o':
            board_state = node.state

            opponent_wins = self.check_winner(board_state, symbol="x")
            ai_wins = self.check_winner(board_state, symbol="o")
            if opponent_wins:
                return -10 + depth
            if ai_wins:
                return 10 - depth

        return 0


    def minimax(self, node, depth, alpha, beta, max_player):
        """
        Laskee rekursiivisesti parhaan mahdollisen
        siirron tulevien siirtojen perusteella.

        Parametrit:
        - node State(): sisältää State objektin
        - depth (int): syvyys, jossa seuraavia siirtoja lasketaan
        - alpha (int): vertailuarvo maksimille
        - beta (int): vertailuarvo minimille
        - max_player (bool): onko kyseessä maksimointi vai minimointi

        Palauttaa:
        - Parhaan siirron ja minimax-arvon
        """


        if depth == 0 or node.is_terminal_state():
            return self.evaluate(node, depth)

        if max_player:
            best_value = -10000
            for child in node.children():
                value = self.minimax(child, depth - 1, alpha, beta, False)
                best_value = max(value, best_value)
                alpha = max(alpha, best_value)
                if best_value >= beta:
                    break
            return best_value
        else:
            best_value = 10000
            for child in node.children():
                value = self.minimax(child, depth - 1, alpha, beta, True)
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
        state = State(board, 'o', self.last_move)
        best_value = -100
        best_move = state.move
        
        for child_state in state.children():
            value = self.minimax(child_state, depth=3, alpha=-10000, beta=10000, max_player=False)
            if value >= best_value:
                best_value = value
                best_move = child_state.move
                
        return best_move

