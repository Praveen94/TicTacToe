import random

def display_board(board):
    print("\n"*30)
    print(board[1]+" | "+board[2]+" | "+board[3])
    print("----------")
    print(board[4]+" | "+board[5]+" | "+board[6])
    print("----------")
    print(board[7]+" | "+board[8]+" | "+board[9])

def player_input():

    marker=''

    while not (marker=="X" or marker=="O"):
        marker=input("Please choose a marker")

        if marker=="X":
            return ("X","O")
        else:
            return ("O","X")

def place_marker(board, marker, position):
    board[position]=marker

def win_check(board, mark):
    for i in range(1,4):

        if all(x==mark for x in board[3*i:(3*i)+3]): #checking all rows
            return True
        # elif all(x==mark for x in board[i::3]): # checking all columns
        #     return mark

        elif ((board[0]==board[3]==board[6]==mark) or (board[1]==board[4]==board[7]==mark) or (board[2]==board[5]==board[8]==mark)):
            return True


        elif all(x==mark for x in board[i::4]): # checking ltr diagonal
            return True
        elif all(x==mark for x in board[i+2:7:2]): # checking rtl diagonal
            return True
        else:
            return False

def choose_first():
    choose=random.randint(0,1)
    if choose==0:
        return "Player 1"
    else:
        return "Player 2"

def space_check(board, position):
    return board[position]==" "

def full_board_check(board):
    for i in range(1,10):
        if board[i]==" ":
            return False
    return True

def player_choice(board):
    position=0
    while position not in range(1,10) and not space_check(board,position):
            position=int(input("Please Enter a position from 1 to 9:"))

    return position

def replay():
    choice=input("Want to replay?Enter 'Yes' or 'No':")
    return choice=="Yes"

while True:
    # Reset the board
    the_board=[" "]*10
    player1marker,player2marker=player_input()
    print("Player 1:{} \n Player 2:{}".format(player1marker,player2marker))
    turn = choose_first()
    print(turn + ' will go first.')

    choice=input("Ready to play? y or n:")

    if choice=='y':
        gameOn=True
    else:
        gameOn=False

    while gameOn:

        if turn=="Player 1":
            display_board(the_board)

            pos=player_choice(the_board)
            place_marker(the_board,player1marker,pos)
            if win_check(the_board,player1marker):
                display_board(the_board)
                print("Player 1 has WON!")
                gameOn=False
                break
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Its a draw")
                    gameOn=False
                    break
                else:
                    turn="Player 2"
        else:
            display_board(the_board)

            pos=player_choice(the_board)
            place_marker(the_board,player2marker,pos)
            if win_check(the_board,player2marker):
                display_board(the_board)
                print("Player 2 has WON!")
                gameOn=False
                break
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("Its a draw")
                    gameOn=False
                    break
                else:
                    turn="Player 1"

    if not replay():
        break