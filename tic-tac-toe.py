# This game is written by : Saeid Shahedi
import random
from IPython.display import clear_output

board = {'9': ' ', '8': ' ', '7': ' ', '6': ' ', '5': ' ', '4': ' ', '3': ' ', '2': ' ', '1': ' '}
board_keys = []
for k in board:
    board_keys.append(k)


def displayboard(board):
    print('--------------')
    print('|' + board['7'] + ' || ' + board['8'] + ' || ' + board['9'] + ' | ')
    print('--------------')
    print('|' + board['4'] + ' || ' + board['5'] + ' || ' + board['6'] + ' | ')
    print('--------------')
    print('|' + board['1'] + ' || ' + board['2'] + ' || ' + board['3'] + ' | ')
    print('--------------')

def choose_first():
    player_list =["player1","player2"]
    turn = random.randint(0,1)
    return player_list[turn]

def player_input():
    player1 = input("Please choose between 'X' and 'O' : ")
    while True:
        if player1.upper() == 'X':
            player2 = 'O'
            print("You've chosen " + player1 + ". Player 2 will be " + player2)
            return player1.upper(), player2
        elif player1.upper() == 'O':
            player2 = 'X'
            print("You've chosen " + player1 + ". Player 2 will be " + player2)
            return player1.upper(), player2
        else:
            player1 = input("Invalid input \t Please just choose between 'X' and 'O' :")


def game():
    player = player_input()
    if player[0] == 'X':
        turn = 'X'
        count = 0
    else:
        turn = 'O'
        count = 0
    for i in range(10):
        displayboard(board)
        print("It's your turn," + turn + ".Move to which place?")
        clear_output(wait=True)
        move = input()


        try:
            if board[move] == ' ':
                board[move] = turn
                count += 1

            else:
                print("That place is already filled.\nMove to which place?")
                continue
        except:
            print("Wrong input \n please only enter the number between (1-9)")
        if count >= 5:
            if board['7'] == board['8'] == board['9'] != ' ':
                displayboard(board)
                print("\nGame Over.\n")
                print(" ** " + turn + " won. **")
                break
            elif board['4'] == board['5'] == board['6'] != ' ':
                displayboard(board)
                print("\nGame Over.\n")
                print(" ** " + turn + " won. **")
                break
            elif board['1'] == board['2'] == board['3'] != ' ':
                displayboard(board)
                print("\nGame Over.\n")
                print(" ** " + turn + " won. **")
                break
            elif board['1'] == board['4'] == board['7'] != ' ':
                displayboard(board)
                print("\nGame Over.\n")
                print(" ** " + turn + " won. **")
                break
            elif board['2'] == board['5'] == board['8'] != ' ':
                displayboard(board)
                print("\nGame Over.\n")
                print(" ** " + turn + " won. **")
                break
            elif board['3'] == board['6'] == board['9'] != ' ':
                displayboard(board)
                print("\nGame Over.\n")
                print(" ** " + turn + " won. **")
                break
            elif board['7'] == board['5'] == board['3'] != ' ':
                displayboard(board)
                print("\nGame Over.\n")
                print(" ** " + turn + " won. **")
                break
            elif board['1'] == board['5'] == board['9'] != ' ':
                displayboard(board)
                print("\nGame Over.\n")
                print(" ** " + turn + " won. **")
                break
        # Draw condition
        if count == 9:
            print("\nGame Over.\n")
            print("Draw match !")
            break
        # changing player turn
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    # replay the game
    restart = input("Do you want to play Again?(y/n)").lower()
    if restart == "y" :
        for key in board_keys:
            board[key] = " "
        game()
    elif restart == "n":
        print("Thank you for choosing our game. \n we wish see you soon again")
    else:
        print("Invalid input")


if __name__ == "__main__":
    print("Welcome to Tic - Tac - Toe playing program \n written by Saeid Shahedi")
    # sample board
    print("The below board is the sample which one you can locate the number :")
    print('--------------')
    print('|' + " 7" + ' || ' + "8" + ' || ' + "9" + ' | ')
    print('--------------')
    print('|' + " 4" + ' || ' + "5" + ' || ' + "6" + ' | ')
    print('--------------')
    print('|' + " 1" + ' || ' + "2" + ' || ' + "3" + ' | ')
    print('--------------')
    game()
