def get_subMatrix_id(i, j):
    if i < 3:
        if j < 3:
            return 0
        if j < 6:
            return 1
        if j < 9:
            return 2

    if i < 6:
        if j < 3:
            return 3
        if j < 6:
            return 4
        if j < 9:
            return 5

    if i < 9:
        if j < 3:
            return 6
        if j < 6:
            return 7
    return 8


class SudokuSolver:
    def __init__(self, board):
        self.board = board
        self.rf = []
        self.cf = []
        self.mf = []
        self.ans = []
        self.isSolved = False

    def main(self):
        self.num_freq_init()
        self.solver(0, 0)
        if self.is_input_valid():
            if self.isSolved:
                return self.ans
            else:
                print('Error')
        else:
            print('INVALID INPUT')

    def num_freq_init(self):
        for r in range(9):
            temp = [0] * 9
            for c in range(9):
                if self.board[r][c] != 0:
                    temp[self.board[r][c] - 1] += 1
            self.rf.append(temp)

        for c in range(9):
            temp = [0] * 9
            for r in range(9):
                if self.board[r][c] != 0:
                    temp[self.board[r][c] - 1] += 1
            self.cf.append(temp)

        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                temp = [0] * 9
                for r1 in range(r, r + 3):
                    for c1 in range(c, c + 3):
                        if self.board[r1][c1] != 0:
                            temp[self.board[r1][c1] - 1] += 1
                self.mf.append(temp)

    def is_input_valid(self):
        row_check = len([num for row in self.rf for num in row if num > 1])
        column_check = len([num for row in self.cf for num in row if num > 1])
        subMatrix_check = len([num for row in self.mf for num in row if num > 1])
        if not row_check and not column_check and not subMatrix_check:
            # 1: input is valid
            return 1
        else:
            # 0: input is invalid
            return 0

    def solver(self, i, j):
        if self.isSolved:
            return
        if i == 9:
            self.isSolved = True
            for row in self.board:
                self.ans.append(row.copy())
            return
        if self.board[i][j] != 0:
            if j + 1 > 8:
                self.solver(i + 1, 0)
            else:
                self.solver(i, j + 1)
            return
        else:
            subMatrix_idx = get_subMatrix_id(i, j)
            for num in range(1, 10):
                if self.rf[i][num - 1] == 0 and self.cf[j][num - 1] == 0 and self.mf[subMatrix_idx][num - 1] == 0:
                    self.board[i][j] = num
                    self.rf[i][num - 1] = 1
                    self.cf[j][num - 1] = 1
                    self.mf[subMatrix_idx][num - 1] = 1

                    if j + 1 > 8:
                        self.solver(i + 1, 0)
                    else:
                        self.solver(i, j + 1)

                    self.board[i][j] = 0
                    self.rf[i][num - 1] = 0
                    self.cf[j][num - 1] = 0
                    self.mf[subMatrix_idx][num - 1] = 0
