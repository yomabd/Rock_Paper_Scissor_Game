"""!python3
@created by yomabd
This is a ROCK, PAPER, SCISSORS GAME
"""
import random
# A function that takes players move and decides if there is a win or tie
def is_winner(computer_move, user_move):
    if computer_move == player_move:
        print('There is a tie!')
        print('Computer Move: %s'%computer_move)
        print('User Move: %s'%player_move)
        return 'tie'
    else:
        if computer_move == 'R' and player_move == 'S' or computer_move == 'P' and player_move == 'R' \
             or computer_move == 'S' and player_move == 'P':
            print('Computer wins!!!')
        else: 
            print("Hurray! You won!!!")
    print('Computer Move: %s'%computer_move)
    print('User Move: %s'%player_move)
    return 'win'
    
#Program implementation begins
print('*************************THIS IS A ROCK - PAPER - SCISSORS GAME***************************')
print('Rules of the game: ')
print("                   Rock beats Scissors")
print("                   Paper beats Rock")
print("                   Scissors beats Paper")
print("                   Tie happens when you play the same move as the computer\n\n")
print("GAMES STARTS NOW....")


#Programs main loop
while True:
    print('R --> ROCK P --> PAPER S --> SCISSORS Q --> QUIT')
    moves =['R','P','S']
    computer_move = random.choice(moves)
    player_move = (input("Play your move:\n")).upper()
    #validation for input
    if player_move not in moves and player_move != 'Q':
        print("Invalid input!!! Please try again...\n")
        continue
    elif player_move == 'Q':
        print('GAME quitted......')
        quit()
    else:
    #check the two moves and decide there is a win or tie
        if is_winner(computer_move,player_move) == 'tie':
            continue
        else:
            print('\nGame has ended....')
            quit()




   



