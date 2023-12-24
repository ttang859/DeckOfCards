#https://bicyclecards.com/how-to-play/blackjack

import random
from card_interface import Player, init, fresh_deck, shuffler, betting_phase, reset_hands

def display_cards(players):
    for p in range(len(players)):
        if p == len(players)-1:
            print('Dealer\'s cards: ' + str(players[p].curr_hand[0].get_card()))
            print('Face Down Card')
        else:
            print('Player ' + str(players[p].get_pid()) + '\'s cards: ')
            players[p].show_cards()
            print('Player ' + str(players[p].get_pid()) + '\'s total: ' + str(players[p].get_total()))

def play_bj(players): #runs a game of blackjack

    #initializing the deck
    deck = fresh_deck()
    for _ in range(1, random.randint(2,6)):
        deck = shuffler(deck)

    #betting phase
    players = betting_phase(players)
    
    #dealing phase
    for _ in range(2):
        for player in players:
            player.curr_hand.append(deck.pop(0))
    
    #display the cards 
    display_cards(players)

    #dealer check for blackjack and filter list of players to see who's values are instantly

    #player's turn: show bal, hit, stand, double down

    #dealer's turn
            
    #outcome
    replay = input('Play Again? Enter Yes or No: ')
    while True:
        if replay.lower() == 'no':
            exit()
        elif replay.lower() == 'yes':
            reset_hands(players) # need to clear current hands
            play_bj(players) #change this to loop back to another function rather than main
        else:
            replay = input('Invalid Entry; Play Again? Enter Yes or No: ')

players = init()
dealer = Player(len(players), [],0,0)
players.append(dealer)
play_bj(players)