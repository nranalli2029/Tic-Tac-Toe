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