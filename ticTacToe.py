class TicTacToe():
    def __init__(self):
        self.board = [["-", "-", "-"], ["-", "-", "-"],["-", "-", "-"]]
        self.current = "O"
        self.gameOver = False

    def print_board(self):
        output = []
        for i in range(len(self.board)):
            output.append(" ".join(self.board[i]))
        return "\n".join(output) + "\n"
    
    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == self.current:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == self.current:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.current:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == self.current:
            return True
        return False

    def make_move(self, x, y):
        if self.board[x][y] == "-":
            self.board[x][y] = self.current
            board = self.print_board()
            if self.is_draw():
                self.gameOver = True
                return f"{board}\nDraw!"
            
            elif self.check_winner():
                self.gameOver = True
                return f"{board}\n{self.current} has won the game!"
            
            else:
                if self.current == "X":
                    self.current = "O"
                else:
                    self.current = "X"
                return self.print_board()
        else:
            return "Space Taken\n"
        
    def is_draw(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == "-":
                    return False
        return True
    
    def get_input(self, rowcol):
        x = input(f"{rowcol}: ")
        if x.isnumeric() and int(x) == float(x) and 1 <= int(x) <= 3:
            return int(x) - 1
        else:
            print(f"\n{rowcol} must be an integer between 1 and 3\n")
            return self.get_input(rowcol)


    def play(self):
        print("\nTic-Tac-Toe\n")
        while not self.gameOver:
            print(f"Turn: {self.current}\n")
            row = self.get_input("Row")
            col = self.get_input("Column")
            print(f"\n{self.make_move(row, col)}")
        reset = input("\nReset (Y/N): ")
        if reset.upper() == "Y" :
            self.reset()

    def reset(self):
        self.board = [["-", "-", "-"], ["-", "-", "-"],["-", "-", "-"]]
        self.current = "O"
        self.gameOver = False
        self.play()