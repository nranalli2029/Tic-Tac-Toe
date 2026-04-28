class TicTacToe():
    def __init__(self):
        self.board = [["-", "-", "-"], ["-", "-", "-"],["-", "-", "-"]]
        self.current = "O"
        self.gameOver = False
        self.scores = {"O": 0, "X": 0}
        self.play()

    def print_board(self): #returns the board as a string
        output = []
        for i in range(len(self.board)):
            output.append(" ".join(self.board[i]))
        return "\n".join(output) + "\n"
    
    def check_winner(self): #Checks for a win in rows, columns, and diagonals
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

    def make_move(self, x, y): #Makes move if space is open and checks the state of the game
        if self.board[x][y] == "-":
            self.board[x][y] = self.current
            board = self.print_board()
            if self.is_draw():
                self.gameOver = True
                return f"{board}\nDraw!"
            
            elif self.check_winner():
                self.gameOver = True
                self.scores[self.current] += 1
                return f"{board}\n{self.current} has won the game!"
            
            else:
                if self.current == "X":
                    self.current = "O"
                else:
                    self.current = "X"
                return self.print_board()
        else:
            return "Space Taken\n"
        
    def is_draw(self): #Checks board for draw
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == "-":
                    return False
        return True
    
    def get_input(self, rowcol): #Gets and validates player intput
        x = input(f"{rowcol}: ").strip()
        if x.isnumeric() and int(x) == float(x) and 0 <= int(x) <= 2:
            return int(x)
        else:
            print(f"\n{rowcol} must be an integer between 0 and 2\n")
            return self.get_input(rowcol)


    def play(self): #Starts the game
        print("\nTic-Tac-Toe\n")
        while not self.gameOver:
            print(f"Turn: {self.current}\n")
            row = self.get_input("Row")
            col = self.get_input("Column")
            print(f"\n{self.make_move(row, col)}")
        print(f"Score:\nO: {self.scores["O"]}\nX: {self.scores["X"]}")
        reset = input("\nReset (Y/N): ")
        if reset.upper() == "Y" :
            self.reset()

    def reset(self): #resets all initial variables
        self.board = [["-", "-", "-"], ["-", "-", "-"],["-", "-", "-"]]
        self.current = "O"
        self.gameOver = False
        self.play()


TicTacToe()