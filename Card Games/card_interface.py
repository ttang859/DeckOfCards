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
    
    def get_card(self):
        return self.card_id, self.suit
    
class Player:
    def __init__(self, pid, curr_hand, curr_bet, bal):
        self.pid = pid
        self.curr_hand = curr_hand #array holding the cards in player's hand
        self.bal = bal #player's balance
        self.curr_bet = curr_bet
        self.hand_val = 0 #total value of player's cards (add function to translate)

    def get_pid(self): #returns a player identifier
        return self.pid

    def get_bal(self): #returns a player's balance
        return self.bal
    
    def get_bet(self):
        return self.curr_bet

    def place_bet(self, amt): #allows player to place a bet, deducts it from balance and 
        self.bal -= amt
        self.curr_bet = amt
        return amt

    def pay_out(self,amt):
        self.bal += amt
        return self.bal

    def show_cards(self):
        for card in self.curr_hand:
            print(card.get_card())

    def get_total(self): #troubleshoot when changing the Ace doesn't do anything (worried it might just subtract 10 when it doesn't need to)
        self.hand_val = 0
        for card in self.curr_hand:
            if Card.denomination[card.get_card_id()] > 10:
                self.hand_val += 10
            else:
                self.hand_val += Card.denomination[card.get_card_id()]
                
        if any(card.get_card_id() == 'A' for card in self.curr_hand): #min, max it with both options
            ace_one = self.hand_val
            ace_eleven = ace_one + 10
            if ace_eleven <= 21:
                self.hand_val = ace_eleven
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
        new_player = Player(p+1,[],0,int(p_bal))
        players.append(new_player)
    return players

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
        bet = input('Enter Bet for Player ' + str(players[p].get_pid()) + ': ')
        while not bet.isdigit():
            bet = input('Please Enter Numerical Bet: ')
        while int(bet) < 0 or int(bet) > players[p].get_bal():
            bet = input('Bet is either too little or too much, enter new bet: ')
        players[p].place_bet(int(bet))
    return players

def reset_hands(players):
    for player in players:
        player.curr_hand = []
        player.curr_bet = 0
        player.hand_val = 0
    return players
