import utils
# import module random
import random

print('Lets Play Rock Paper Scissors!')
player_name = input('Enter your name: ')

print('Choose Hand: (0: Rock, 1: Paper, 2: Scissors)')
player_hand = int(input('Enter Number (0-2): '))

if utils.validate(player_hand):
    # Tetapkan nomor acak antara 0 dan 2 ke computer_hand menggunakan randint
    computer_hand = random.randint(0,2)
    
    utils.print_hand(player_hand, player_name)
    utils.print_hand(computer_hand, 'Computer')

    result = utils.judge(player_hand, computer_hand)
    print('result: ' + result)
else:
    print('Please enter right Number')
