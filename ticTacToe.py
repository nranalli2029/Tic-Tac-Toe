class TicTacToe():
    def __init__(self):
        self.board = [["-", "-", "-"], ["-", "-", "-"],["-", "-", "-"]]
        self.current = "O"
        self.gameOver = False

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
        
    def is_draw(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == "-":
                    return False
        return True