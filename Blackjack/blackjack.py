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
    def __init__(self, num_cards, curr_hand, bal):
        self.num_cards = num_cards #number of cards in hand
        self.curr_hand = curr_hand #array holding the cards in player's hand
        self.hand_val = 0 #total value of player's cards
        self.bal = bal #player's balance
    def get_bal(self):
        return self.bal
    
    def bet(self, amt):
        if amt <= 0:
            print('Bet has to be more than 0 ')
        while not amt.isdigit:
            amt = input('Enter numerical amount: ')
        self.bal -= amt
        return amt

    def get_cards(self):
        for card in self.curr_hand:
            print(card.get_card_id)

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
    deck = fresh_deck()
    for card in deck:
        print(card.card_id)
        print(card.value)
        print(card.suit)
    for _ in range(1, random.randint(2,6)):
        deck = shuffler(deck)
    print('shuffled:')
    for card in deck:
        print(card.card_id)
        print(card.value)
        print(card.suit)

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