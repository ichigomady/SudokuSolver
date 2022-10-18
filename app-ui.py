from solver import SudokuSolver
import tkinter as tk
from PIL import Image, ImageTk


class SudokuGui:
    def __init__(self):
        self.root = tk.Tk()
        self.color = '#f8edeb'
        self.solve_btn_color = '#ffd7ba'
        self.entry_box_color = '#E4E3E3'
        self.display_configure()
        self.user_input()
        self.root.mainloop()

    def display_configure(self):
        self.root.title('Sudoku Solver')
        self.root.configure(background=self.color)
        self.root.minsize(600, 600)
        self.root.maxsize(600, 600)

        self.logo = Image.open(r'logo\logo.jpg')
        self.logo = ImageTk.PhotoImage(self.logo)
        self.logo_label = tk.Label(image=self.logo)
        self.logo_label.image = self.logo
        self.logo_label.place(x=100, y=0)

    def user_input(self):
        self.instruction1_lbl = tk.Label(self.root, text='Instructions: \nEnter each rows\'s data below. Please use 0 for blank spaces. Each number must be comma seperated.\n For eg: Row 1-> 8, 0,  0,  4,  0,  2,  0,  3,  0', background=self.color)
        self.instruction1_lbl.place(x=15, y=80)
        self.row_lbl = [0] * 10
        self.row_entry = [0] * 10
        self.y_pos = 145
        for i in range(9):
            self.row_lbl[i] = tk.Label(self.root, text=f'Row {i+1}', background=self.color)
            self.row_lbl[i].place(x=150, y=self.y_pos)
            self.row_entry[i] = tk.Entry(self.root, width=50, background=self.entry_box_color)
            self.row_entry[i].place(x=200, y=self.y_pos)
            self.y_pos += 25

        self.y_pos += 15
        self.submit_btn = tk.Button(self.root, text='SOLVE', background=self.solve_btn_color, command=self.get_input)
        self.submit_btn.place(x=225, y=self.y_pos, width=150)

    def get_input(self):
        board = []
        isInputCorrect = True
        for i in range(9):
            try:
                temp = self.row_entry[i].get()
                temp = list(map(int, temp.split(',')))   
                board.append(temp)
            except:
                self.error_lbl = tk.Label(self.root, text='ERROR: Please check your input', background=self.color)
                self.error_lbl.place(x=215, y=self.y_pos+30)
                isInputCorrect = False
                break
        self.submit_btn["state"] = 'disabled'
        if isInputCorrect:
            self.solve_sudoku(board)
    
    def solve_sudoku(self, board):
        solve_this = SudokuSolver(board)
        answer = solve_this.main()
        # print(answer)
        self.display_output(answer)
    
    def display_output(self, answer):
        self.y_pos += 30
        self.output_lbl = tk.Label(self.root, text='Here is your solved Sudoku Board:', background=self.color)
        self.output_lbl.place(x=200, y=self.y_pos)
        
        x_ = 200
        y_ = self.y_pos + 30
        for i, row in enumerate(answer):
            r_lbl = tk.Label(self.root, text=f'Row {i+1}:', background=self.color)
            r_lbl.place(x=x_, y=y_)

            x_ += 50

            for num in row:
                num_lbl = tk.Label(self.root, text=str(num), background=self.color)
                num_lbl.place(x=x_, y=y_)
                x_ += 15
            x_ = 200
            y_ += 15



        


def main():
    # sudoku = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
    #         [6, 0, 0, 1, 9, 5, 0, 0, 0],
    #         [0, 9, 8, 0, 0, 0, 0, 6, 0],
    #         [8, 0, 0, 0, 6, 0, 0, 0, 3],
    #         [4, 0, 0, 8, 0, 3, 0, 0, 1],
    #         [7, 0, 0, 0, 2, 0, 0, 0, 6],
    #         [0, 6, 0, 0, 0, 0, 2, 8, 0],
    #         [0, 0, 0, 4, 1, 9, 0, 0, 5],
    #         [0, 0, 0, 0, 8, 0, 0, 7, 9]
    #         ]
    gui = SudokuGui()


if __name__ == '__main__':
    main()

