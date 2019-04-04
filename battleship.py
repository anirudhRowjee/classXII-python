# battleship
import pprint

class board:

    def __init__(self, row_col_val):
        self.board = []
        for i in range(0, row_col_val):
            row = ['*' for x in range(0, row_col_val)]
            self.board.append(row)

    def get_board(self):
        return self.board

    def print_board(self):
        for row in self.board:
            print(row)

class team:
    


class player:

    def __init__(self, playername, team):
        self.playername = playername
        self.points = 0
        self.team = team


b = board(5)
b.print_board()
        
