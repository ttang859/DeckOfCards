import random

class Card:
    denomination = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
    suits = {'Spade': 1, 'Heart': 2, 'Club': 3, 'Diamond': 4}

    def __init__(self, card_id, suit):
        self.card_id = card_id #suit and number    
        self.suit = suit #diamond, clover, heart, spade

    def get_card_id(self):
        return self.card_id
    def get_suit(self):
        return self.suit
    
class Player:
    def __init__(self, curr_hand, curr_bet, bal):
        self.curr_hand = curr_hand #array holding the cards in player's hand
        self.bal = bal #player's balance
        self.curr_bet = curr_bet
        self.hand_val = 0 #total value of player's cards (add function to translate)
    def get_bal(self):
        return self.bal
    
    def place_bet(self, amt):
        self.bal -= amt
        self.curr_bet = amt
        return amt

    def show_cards(self):
        for card in self.curr_hand:
            print(card.get_card_id() + ' ' + card.get_suit())

    def get_total(self):
        for card in self.curr_hand:
            if card.get_card_id() == 'J' or card.get_card_id() == 'Q'or card.get_card_id() == 'K':
                self.hand_val += 10
            else:
                self.hand_val += Card.denomination.get(card.get_card_id())
                
        if any(card.get_card_id() == 'A' for card in self.curr_hand): #check for value of Ace since it depends on overall hand value
            if self.hand_val < 21: #for when a player has a soft hand (i.e. when the Ace represents a 1)
                self.hand_val += 10 
            elif self.hand_val > 21: #for when a player has an Ace that was an 11 but could benefit from it being lower
                self.hand_val -= 10
        return self.hand_val
    # @staticmethod
    # def action_hit(self):
    #     pass

    # @staticmethod
    # def action_double(self):
    #     pass
    
    # @staticmethod
    # def action_split():
    #     pass

def fresh_deck():
    deck = []
    for card_num in Card.denomination:
        for card_suit in Card.suits:
            deck.append(Card(card_num, card_suit))
    return deck

def shuffler(deck):
    shuffled_deck = []
    for _ in range(52):
        rand_ind = random.randint(0,len(deck)-1)
        if not deck[rand_ind] in shuffled_deck:
            shuffled_deck.append(deck[rand_ind])
        deck.pop(rand_ind)
    return shuffled_deck

def betting_phase(players): #iterates through the list of players to give each a chance to bet; excludes the dealer
    for p in range(len(players)-1): 
        bet = input('Enter Bet for Player ' + str(p+1) + ': ')
        while not bet.isdigit():
            bet = input('Please Enter Numerical Bet: ')
        while int(bet) < 0 or int(bet) > players[p].get_bal():
            bet = input('Bet is either too little or too much, enter new bet: ')
        players[p].place_bet(int(bet))
    return players

def init(): #initializes the game with number of players and each of their balances
    num_players = input('Enter number of players: ')
    if not num_players.isdigit:
        init()
    players = []
    for p in range(int(num_players)):
        while True:
            p_bal = input('Please enter balance for Player ' + str(p+1) + ': ')
            if p_bal.isdigit:
                break
        new_player = Player([],0,int(p_bal))
        players.append(new_player)
    return players

def reset_hands(players):
    for player in players:
        player.curr_hand = []
        player.curr_bet = 0
        player.hand_val = 0
    return players
