import random


j1 = input('qui est le j1 : ')
j2 = input('qui est le j2 : ')

class Morpion:

    def __init__(self):
        self.board = []

    def create_board(self, n):
        for i in range(n):
            row = []
            for j in range(n):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):
        win = None
        
        n = len(self.board)
        
        if player == j1:
            player = 'X'
        else:
            player = 'O'

        # check les lignes 
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # check les colonnes
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # check les diagonales
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return j1 if player == j2 else j2

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
       
        
        choice_format = int(input('Choisi la taille du tableau (3, 4, 5...) : '))
        self.create_board(choice_format)

        player = j1 if self.get_random_first_player() == 1 else j2
        while True:
            print(f"\nAu tour du joueur {player} : ")

            self.show_board()

            # prendre la valeur du joueur
            row, col = list(
                map(int, input("Choisi une ligne et une colonne : ").split()))

            # mettre le X ou le O 
            if player == j1:
                self.fix_spot(row - 1, col - 1, 'X')
            else:
                self.fix_spot(row - 1, col - 1, 'O')

            # check si le joueur gagne
            if self.is_player_win(player):
                print(f"{player} gagne!")
                break

            # check si tout est remplies
            if self.is_board_filled():
                print("Egalitée !")
                break

            # changement de joueur
            player = self.swap_player_turn(player)

        # montrer le tableau final
        print()
        self.show_board()


# lance le jeu
morpion = Morpion()
morpion.start()
