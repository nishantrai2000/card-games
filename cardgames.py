import random
import time
values = ['Ace'] + [str(n) for n in range (2,11)] + ['J','Q','K']
suits = ['Hearts','Diamonds','Clubs','Spades']

class Card:


    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return self.value + ' of ' + self.suit

    def value(self):
        return self.value
    
    def suit(self):
        return self.suit
        

class Deck:


    def __init__(self):
        self.cards = [Card(suit, value) for suit in suits for value in values]
        return self.cards
 
    def __str__(self):
        s = ''
        for i in range(len(self.cards)):
            s += ' ' * i + str(self.cards[i]) + '\n'
        return s

    def deal_top_card(self):
        card = self.cards.pop(0)
        return card
    
    def deal_random_card(self):
        card = random.choice(self.cards)
        self.cards.pop(card)
        return card

    def shuffle(self):
        print('Shuffling deck...\n')
        random.shuffle(self.cards)
        time.sleep(2)
        print('Deck has been shuffled.\n')
        return self.cards

    def deal_hands(self, hands, amount=999):
        num_hands = len(hands)
        print('Dealing %d hands...'%(num_hands))
        time.sleep(2)
        for i in range(amount):
            if self.is_empty():
                print('Deck is empty!\n')
                break
            card = self.pop()
            hand = hands[i % num_hands]
            hand.add(card)
        print(num_hands + ' hands have been dealt.\n')
        
    
    def is_empty(self):
        if len(self_cards) == 0:
            return True
        else:
            return False


class Hand(deck):


    def __init__(self, name = ''):
        self.cards = []
        self.name = name
    
    def __str__(self):
        s = 'Hand ' + self.name
        if self.is_empty():
            s = s + ' is empty.\n'
        else:
            s = s + ' contains:\n' + self
            return Deck.__str__(self)

    def add(self,card):
        self.cards.append(card)
    

class CardGame:


    def __init__(self):
        deck = Deck()
        deck.shuffle()


class RollingStoneGame(CardGame):

    
    def play(self, names):
        
        

    






