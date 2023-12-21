import card_setup
import random


def init():
    num_players = input('Enter number of players: ')
    if not num_players.isdigit:
        init()
    players = []
    for p in range(int(num_players)):
        while True:
            p_bal = input('Please enter balance for Player ' + str(p) + ': ')
            if p_bal.isdigit:
                break
        new_player = Player(0,[],p_bal)
        players.append(new_player)
    #dealer is added last
    dealer = Player(0,[],0)
    players.append(dealer)
    return players



def gameplay(players):
    #create stack that is the shuffled deck, do initial dealing, hits and stands, dealer hits, monetary values (array of tuples maybe)
    
    #initializing the deck (point where we recurse back?)
    deck = Shuffler()

    #betting phase

    #dealing phase

    #hit, stand, double down, split

    replay = input('Play Again? Enter Yes or No: ')
    while True:
        if replay.lower() == 'no':
            exit()
        elif replay.lower() == 'yes':
            gameplay() #change this to loop back to another function rather than main
        else:
            replay = input('Invalid Entry; Play Again? Enter Yes or No: ')


players = init()
gameplay(players)