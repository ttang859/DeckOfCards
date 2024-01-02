import random, math
from card_interface import Player, init, fresh_deck, shuffler, betting_phase, reset_hands

def display_cards(players):
    for player in players:
        if player.get_pid() == 0:
            print('Dealer\'s cards: ' + str(player.curr_hand[0].get_card()))
            print('Face Down Card')
        else:
            print('Player ' + str(player.get_pid()) + '\'s cards: ')
            player.show_cards()
            print('Player ' + str(player.get_pid()) + '\'s total: ' + str(player.get_total()))

def play_again(players):
    replay = input('Play Again? Enter Yes or No: ')
    while True:
        if replay.lower() == 'no':
            break
        elif replay.lower() == 'yes':
            reset_hands(players) # need to clear current hands
            play_bj(players) #change this to loop back to another function rather than main
        else:
            replay = input('Invalid Entry; Play Again? Enter Yes or No: ')

# def player_action(players, card):
#     for player in players:
#         if(player.get_pid() == dealer.get_pid()):
#             break
#         while True:
#             if player.get_total() >= 21:
#                 break
#             options = input('Player ' + str(player.get_pid()) + ', Hit (H), Stand (S) or Double Down (DD)?: ')
#             if options.upper() == 'S':
#                 break
#             elif options.upper() == 'H':
#                 player.curr_hand.append(card) #hit
#                 print(str(player.curr_hand[len(player.curr_hand)-1].get_card()) + ' ' + str(player.get_total()))
#                 if player.get_total() >= 21:
#                     pass
#             elif options.upper() == 'DD':
#                 pass
#             else:
#                 print('Incorrect Input')

def player_pay_outs(player, dealer):
    if player.get_total() <= 21:
        if player.get_total() == 21 and len(player.curr_hand) == 2: #rewarding for a blackjack
            player.pay_out(math.ceil(player.get_bet()*2.5))
        elif dealer.get_total() > 21 or (player.get_total() > dealer.get_total()): #for when dealer busts or player beats dealer
            player.pay_out(player.get_bet()*2)
        elif player.get_total() == dealer.get_total(): #a tie so tied players get their money back
            player.pay_out(player.get_bet())
    return player

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
            player.curr_hand.append(deck.pop(0)) #hit
    
    #display the cards 
    display_cards(players)

    #dealer check for blackjack and filter list of players to see who's values are instantly
    dealer = players[len(players)-1]

    if dealer.get_total() == 21:
        print('Dealer has hit a Blackjack')
        dealer.show_cards()
        players = list(map(lambda p: p.pay_out(p.get_bet()) if p.get_total() == 21 else p.get_total() != 21, players)) #need to check to see if this actually works
        for player in players:
            print(str(player.get_pid()) + ' ' + str(player.get_bal()))
        play_again(players)

    #player's turn: show bal, hit, stand, double down
    # player_action(players, deck.pop(0))
    for player in players:
        if(player.get_pid() == dealer.get_pid()):
            break
        while True:
            if player.get_total() >= 21:
                break
            options = input('Player ' + str(player.get_pid()) + ', Hit (H), Stand (S) or Double Down (DD)?: ')
            if options.upper() == 'S':
                break
            elif options.upper() == 'H':
                player.curr_hand.append(deck.pop(0)) #hit
                print(str(player.curr_hand[len(player.curr_hand)-1].get_card()) + ' ' + str(player.get_total()))
            elif options.upper() == 'DD':
                if player.get_total() >= 9 and player.get_total() <= 11:
                    print('Player ' + str(player.get_pid()) + ' has doubled down')
                    player.pay_out(player.get_bet())
                    player.place_bet(player.get_bet()*2)
                else:
                    print('Unable to double down')
            else:
                print('Incorrect Input')

    #dealer's turn
    while dealer.get_total() <= 16:
        dealer.curr_hand.append(deck.pop(0)) #hit
        print('Dealer: ' + str(dealer.curr_hand[len(dealer.curr_hand)-1].get_card()))
    print('Dealer: ')
    dealer.show_cards()
    print(dealer.get_total())

    #pay outs
    #filter out players who busted; if dealer busted pay everyone, if dealer did not bust, pay only those who were higher, if dealer hit blackjack, payback those who have 21 ()
    players = list(map(lambda p: player_pay_outs(p,dealer), players))
    for player in players:
        if player.get_pid() != dealer.get_pid():
            print('Player ' + str(player.get_pid()) + ': ' + str(player.get_bal()))

    play_again(players)

