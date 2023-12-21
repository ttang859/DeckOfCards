import random

class Card:
    nums = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
    suits = {'Spade': 1, 'Heart': 2, 'Club': 3, 'Diamond': 4}
    def __init__(self, card_id, value, suit):
        self.card_id = card_id #suit and number    
        self.value = value #actual value
        self.suit = suit #diamond, clover, heart, spade

    def get_card_id(self):
        return self.card_id
    def get_value(self):
        return self.value
    def get_suit(self):
        return self.suit
    
class Player:
    def __init__(self, num_cards, curr_hand, curr_bet, bal):
        self.num_cards = num_cards #number of cards in hand
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

    def get_cards(self):
        for card in self.curr_hand:
            print(card.get_card_id() + ' ' + card.get_suit())

    # @staticmethod
    # def hit(self):
    #     pass

    # @staticmethod
    # def double(self):
    #     pass
    
    # @staticmethod
    # def split():
    #     pass
def fresh_deck():
    deck = []
    for card_num in Card.nums:
        for card_suit in Card.suits:
            deck.append(Card(card_num, Card.nums.get(card_num), card_suit))
    return deck


def shuffler(deck):
    shuffled_deck = []
    for _ in range(52):
        rand_ind = random.randint(0,len(deck)-1)
        if not deck[rand_ind] in shuffled_deck:
            shuffled_deck.append(deck[rand_ind])
        deck.pop(rand_ind)
    return shuffled_deck

def betting_phase(players):
    for p in range(len(players)-1):
        bet = input('Enter Betting Amount: ')
        while not bet.isdigit():
            bet = input('Please Enter Numerical Bet: ')
        while int(bet) < 0 or int(bet) > players[p].get_bal():
            bet = input('Bet is either too little or too much, enter new bet: ')
        players[p].place_bet(int(bet))
    return players
        

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
        new_player = Player(0,[],0,int(p_bal))
        players.append(new_player)
    #dealer is added last
    dealer = Player(0,[],0,0)
    players.append(dealer)
    return players


def play_bj(players):
    #initializing the deck
    deck = fresh_deck()
    for _ in range(1, random.randint(2,6)):
        deck = shuffler(deck)

    #betting phase
    players = betting_phase(players)
    for player in players:
        print(player.get_bal())
        print(player.curr_bet)
    #dealing phase

    #hit, stand, double down, split

    replay = input('Play Again? Enter Yes or No: ')
    while True:
        if replay.lower() == 'no':
            exit()
        elif replay.lower() == 'yes':
            play_bj(players) #change this to loop back to another function rather than main
        else:
            replay = input('Invalid Entry; Play Again? Enter Yes or No: ')


players = init()
play_bj(players)