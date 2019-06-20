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

    def print_board


b = board(5)
print(b.get_board())
        
