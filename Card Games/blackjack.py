import random
from card_interface import init, fresh_deck, shuffler, betting_phase, reset_hands, Player

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
            #filter list of players to see who's values are instantly 
    for p in range(len(players)):
        if p == len(players)-1:
            print('Dealer\'s cards: ' + str(players[p].curr_hand[0].get_card_id()) + ' ' + str(players[p].curr_hand[0].get_suit()))
            print('Face Down Card')
        else:
            print('Player ' + str(p+1) + '\'s cards: ')
            players[p].show_cards()
            print('Player ' + str(p+1) + '\'s total: ' + str(players[p].get_total()))
    

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
dealer = Player([],0,0)
players.append(dealer)
play_bj(players)