## My First Game in Python :)

from random import shuffle

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def user_guess():
    guess = ''

    while guess not in ['0','1','2']:
        guess=input('Input an index from 0,1,2: ')

    return int(guess)


def guess_game(mylist,guess):
    if mylist[guess] == 'O':
        print("Right Guess!! You Won!!")
    else:
        print("Wrong!!!")
        print(mylist)


def play_game():
    want_to_play=True
    while want_to_play == True:
        my_list = [' ', 'O', ' ']
        mixedup_list = shuffle_list(my_list)
        guess = user_guess()
        guess_game(mixedup_list,guess)
        want_to_play_str=input('Do you want to play again : ( T/F) :: ')
        if(want_to_play_str == 'T'):
            want_to_play=True
        else:
            want_to_play=False

play_game()

