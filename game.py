
class TicTacToe:
    def __init__(self, size=3):
        self.size = size
        self.board = [" "] * (self.size ** 2)
        self.padwidth = len(str(self.size ** 2))

        self.cur_winner = None

    def print_board(self):
        for row in [self.board[i*self.size:(i+1)*self.size] for i in range(self.size)]:
            print("| " + " | ".join(row) + " |")

    def print_board_nums(self):
        number_board = [[f"{i:{self.padwidth}d}" for i in range(j*self.size, (j+1)*self.size)] 
                        for j in range(self.size)]
        for row in number_board:
            print("| " + " | ".join(row) + " |")

    def get_cur_winner(self):
        return self.cur_winner

    def set_cur_winner(self, cur_winner):
        self.cur_winner = cur_winner

    def get_available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def has_empty_squares(self):
        return " " in self.board

    def get_num_empty_squares(self):
        return self.board.count(" ")

    def make_move(self, square, letter):
        if self.board[square] == " ":
            self.board[square] = letter
            if self.is_winner(square, letter):
                self.cur_winner = letter
            return True
        return False

    def is_winner(self, square, letter):
        row_i = square // self.size
        row = self.board[row_i*self.size: (row_i+1)*self.size]

        col_i = square % self.size
        col = [self.board[col_i + i*self.size] for i in range(self.size)]

        diagonal_1_i = [i*self.size + i for i in range(self.size)]
        diagonal_1 = [self.board[i] for i in diagonal_1_i]

        # e.g. self.size = 4
        #      => self.size - 1 = 3
        #      => [1*3, 2*3, 3*3, 4*3] = [3, 6, 9, 12]
        diagonal_2_i = [i*(self.size - 1) for i in range(1, self.size+1)]
        diagonal_2 = [self.board[i] for i in diagonal_2_i]
        
        return all([spot == letter for spot in row]) \
            or all([spot == letter for spot in col]) \
            or all([spot == letter for spot in diagonal_1]) \
            or all([spot == letter for spot in diagonal_2])
