import list_lib

# Tick-Tac-Toe : Using Objects.
#
# Object Oriented Programming (OOP) - Structured programming paradigm.
#   Gives a way to organize your programs into categories called classes.
#
#
#   game = TikTacToe()  ---> Creates a TikTacToe object, which allows one to
#                            use all of the TikTacToe features.
#
# Attributes or Fields are variables that are internal to the class,
# and can be used throughout each function (methods) in the class.
#
# Encapsulation ---> Hiding stuff from the programmer.

class TikTacToe:    
    # Initializer, but is usually called the constructor.
    def __init__(self, board = [[(r,c,'*') for c in range(4)] for r in range(4)]):
        # Global constants, not able to be updated.
        self.blank_sym = '*'
        self.player_syms = ['O', 'X']
        
        self.board = board 
        self.current_player = "X"
        

    # Returns True if self.board is solved, and false otherwise.
    def isSolved(self):
        _solved = [self.blank_sym for row in self.board for (r,c,s) in row if s == self.blank_sym]
        return _solved == []

    # Returns True if current_player is the winner, and false otherwise.
    def checkWinner(self):
        self.board_bool = [[(r,c,s == self.current_player) for (r,c,s) in row] for row in self.board]
        row_bool   = [list_lib.all ([b for (r,c,b) in row]) for row in self.board_bool]
        row_win    = list_lib.any (row_bool)

        colums = [[b for row in self.board_bool for (r,c,b) in row if c == col] for col in [0,1,2]]
        col_bool = [list_lib.all(colums)]
        col_win = list_lib.any (col_bool)

        main_diag = [b for row in self.board_bool for (r,c,b) in row if r == c]
        main_diag_win = list_lib.all (main_diag)

        antidiag = [b for row in self.board_bool for (r,c,b) in row if c == 2 - r]
        antidiag_win = list_lib.all(antidiag)

        return row_win or col_win or main_diag_win or antidiag_win

    # Convert the self.board into a string to be printed to the screen for the
    # user.
    def board2String(self):
        output = ""

        for row in self.board:
            output += "|"
            for (_,_,d) in row:
                output += d + "|"
            output += "\n"

        return output

    # Updates the player:
    def updatePlayer(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'

    # Asks the user for their next move:
    def getNextMove(self):
        row = 0
        col = 0
        correct_input = False

        print("Player "+self.current_player+"'s move.")    
        while not correct_input:
            row = int(input("Enter the row: "))
            if not (0 <= row <= 3):
                print("Invalid input, please enter a row between 0 and 3.")
                continue
            correct_input = True

        correct_input = False
        while not correct_input:
            col = int(input("Enter the col: "))    
            if not (0 <= col <= 3):
                print("Invalid input, please enter a col between 0 and 3.")
                continue

            correct_input = True

        return (row,col)

    def updateBoard(self,row, col):
        self.board[row][col] = (row,col,self.current_player)
        return self.board
    
# Main loop: offically play a game.
def play():       
    game = TikTacToe()        

    while True:                
        print(game.board2String())

        (row,col) = game.getNextMove()

        game.updateBoard(row, col)
        
        if game.isSolved(): break

        game.updatePlayer()

    print(game.board2String())
    win = game.checkWinner()
    if win:
        print (game.current_player+" won!")
    else:
        game.updatePlayer()
        win = game.checkWinner()
        if win:
            print (game.current_player+" won!")
        else:
            print("Error occured")

play()

# if __name__ == "__main__":
#     play()
