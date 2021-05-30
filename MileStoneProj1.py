## Tic Tac Problems

def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])

def player_input():
    choice = 'Wrong'

    while choice not in ['X','O']:
        choice=input("Please select a marker from X or O : ")
        if choice not in ['X','O']:
            print("Please select a valid marker!")
    if choice == 'X':
        return ('X','O')
    else:
        return ('O','X')


def place_marker(board, marker, position):
    board[position]=marker
    return board

def win_check(board,marker):
    if (board[1]==board[2]==board[3]==marker or board[4]==board[5]==board[6]==marker or board[7]==board[8]==board[9]==marker):
        return True
    elif (board[1]==board[4]==board[7]==marker or board[2]==board[5]==board[8]==marker or board[3]==board[6]==board[9]==marker):
        return True
    elif (board[1]==board[5]==board[9]==marker or board[3]==board[5]==board[7]==marker):
        return True
    else:
        return False

import random

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in range(1,10) or not space_check(board,position):
        position = int(input("Input next position from 1-9: "))
        if position not in range(1,10):
            print("Enter Valid Position!!")
        elif not space_check(board,position):
            print("Selected position is not empty!!")

    return position

def replay():
    choice = input("Play Again?? Enter Yes or No: ")
    return choice == 'Yes'


print('Welcome to Tic Tac Toe!')

while True:
    # Set the Game
    game_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    display_board(game_board)
    player1_marker , player2_marker = player_input()
    player_turn = choose_first()
    print(player_turn + ' will go first')

    ## Game Play
    play_game = input("Ready to play? y or n")
    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if player_turn == 'Player 1':
            # Show the board
            display_board(game_board)
            # Choose a position
            position = player_choice(game_board)
            # Place marker on the position
            place_marker(game_board,player1_marker,position)
            # check if won
            if win_check(game_board,player1_marker):
                display_board(game_board)
                print("PLAYER 1 HAS WON!!!")
                game_on = False
            else:
            # check if tie
                if full_board_check(game_board):
                    display_board(game_board)
                    print("TIE GAME!!")
                    game_on = False
                else:
                    player_turn = 'Player 2'
            # no tie or win then next players turn
        else:
            # Show the board
            display_board(game_board)
            # Choose a position
            position = player_choice(game_board)
            # Place marker on the position
            place_marker(game_board, player2_marker, position)
            # check if won
            if win_check(game_board, player2_marker):
                display_board(game_board)
                print("PLAYER 2 HAS WON!!!")
                game_on = False
            else:
                # check if tie
                if full_board_check(game_board):
                    display_board(game_board)
                    print("TIE GAME!!")
                    game_on = False
                else:
                    player_turn = 'Player 1'
    ## Break out if users do not want to play again
    if not replay():
        break
