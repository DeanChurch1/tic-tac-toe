#Dean Church
#Tic-tac-toe


#constants
X = "X"
O = "O"
EMPTY = ''
TIE = "TIE"
NUM_SQUARES = 9

#instructions
def display_instructions():
    print("Welcome player to tic tac toe")
    print("To play tic tac toe you have to fill in a board by entering a number 0-8.\nNumbers will correspond.")
    
    print("""             0 | 1 | 2
            ----------
             3 | 4 | 5
            ----------
             6 | 7 | 8""")
    print("Good luck user")

display_instructions()


def ask_yes_no(question):
    response = None
    while response not in ("y","n"):
        response = input(question).lower()
    return response


def ask_num(question,low,high):
    response = "9999"
    while True:
        if response.isdigit():
            if int(response) in range(low,high):
                break
            else:
                response = input(question)
        else:
            print("you must enter a number")
            response = input(question)
    return int(response)
        

def pieces():
    go_first = ask_yes_no("Do you want to go first(y,n)")
    if go_first == 'y':
        print("\nNeed a little help")
        human = X
        computer = O
    else:
        print("\nThat confident")
        human = O
        computer = X
    return human,computer



def new_board():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board
new_board()




def display_board(board):
    print("\n\t",board[0],"|",board[1],'|',board[2])
    print("\t","-------")
    print("\t",board[3],'|',board[4],"|",board[5])
    print('\t',"-------")
    print('\t',board[6],'|',board[7],'|',board[8],'\n')



def legal_moves(board):
    moves = []
    for square in range(len(board)):
        if board[square] == EMPTY:
            moves.append(square)
    return moves
    


def winner(board):
    WAYS_TO_WIN = ((0,1,2),
        (3,4,5),
        (6,7,8),
        (0,3,6),
        (1,4,7),
        (2,5,8),
        (0,4,8),
        (2,4,6))
    
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None




def human_move(board,human):
    move = None
    legal = legal_moves(board)
    while move not in legal:
        move = ask_num("Where will you move(0-8):",0,NUM_SQUARES)
        if move not in legal:
            print("\nTrying illegal moves.Choose another.\n")
    print("Whatever")
    return move

x = new_board()
c,h = pieces()
placement = human_move(x,h)
print(placement)



def next_turn(turn):
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner,human,computer):
    if the_winner != TIE:
        print(the_winner,"won\n")
    else:
        print("It's a tie\n")
        
    if the_winner == computer:
        print("You weren't good enough")
        
    elif the_winner == human:
        print("You got lucky")
        
    elif the_winner == TIE:
        print("Well you didn't win")
        

def computer_move(board,human,computer):
    board = board[:]
    BEST_MOVES = (4,0,2,6,8,1,3,5,7)
    print("I shall take square number", end=" ")
    #if computer cna win take that move
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        #done checking this move,undo it
        board[move] = EMPTY
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        #done checking this move,undo it
        board[move] = EMPTY
        
#since no one can win on next move, pick best open square
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move


    




    


