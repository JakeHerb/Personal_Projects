#Tic Tac Toe Game
import random

#prints the board with current values
def show_board():
    print board[0], "|", board[1], "|", board[2]
    print "---------"
    print board[3], "|", board[4], "|", board[5]
    print "---------"
    print board[6], "|", board[7], "|", board[8]

#Asks where youd like to go, replaces that spot with an X
def player_turn():
    turn_over = False
    while turn_over == False:
        input = raw_input("Choose your spot: ")
        input = int(input)
        if board[input] == "X" or board[input] == "O":
            print "You can't go there."
            
        else:
                board[input] = ("X")
                turn_over = True

#computer chooses a random spot, if not open, chooses again til open
def comp_turn():
    spot_taken = False
    while spot_taken == False:
        comp_spot = random.randint(0, 8)
        if board[comp_spot] != "X" and board[comp_spot] != "O":
            board[comp_spot] = "O"
            spot_taken = True
            
        else:
            pass
            
        print ""

#checks if 3 given spots are owned by the same player        
def check_line(letter, spot1, spot2, spot3):
    if letter == board[spot1] and letter == board[spot3] and letter == board[spot3]:
        win_check = True
        return win_check
    else:
        return False

#uses check_line for each combonation of winning spots
def lines(letter):
    if check_line(letter, 0, 1, 2) == True:
        print str(letter) + " WINS!"
        return True
    if check_line(letter, 3, 4, 5) == True:
        print str(letter) + " WINS!"
        return True
    if check_line(letter, 0, 3, 6) == True:
        print str(letter) + " WINS!"
        return True
    if check_line(letter, 1, 4, 7) == True:
        print str(letter) + " WINS!"
        return True
    if check_line(letter, 2, 5, 8) == True:
        print str(letter) + " WINS!"
        return True
    if check_line(letter, 0, 4, 8) == True:
        print str(letter) + " WINS!"
        return True
    if check_line(letter, 6, 4, 2) == True:
        print str(letter) + " WINS!"
        return True
    else:
        return False

#Defines what constitutes a single game round
def game():
    show_board()
    player_turn()
    comp_turn()
    show_board()
    while lines("X") == False and lines("O") == False:
        player_turn()
        show_board()
        comp_turn()
        show_board()
#sets the boards values equal to their place in the array
def make_board():
    board = [0, 1, 2,
             3, 4, 5,
             6, 7, 8]
    return board
#this part is the actual game
again = "y"
while again == "y":
    board = make_board()
    game()
    again = raw_input("Would you like to play again? y/n?")
