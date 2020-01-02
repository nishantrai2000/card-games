import random
import time
from enum import Enum

values = ['Ace'] + [str(n) for n in range (2,11)] + ['J','Q','K']


class Suit(Enum):
    Hearts = 'Hearts'
    Diamonds = 'Diamonds'
    Spades = 'Spades'
    Clubs = 'Clubs'


class Card:


    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return self.value + ' of ' + self.suit
        

class Deck:


    def __init__(self):
        self.cards = [Card(suit, value) for suit in Suit for value in values]
 
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
            card = self.cards.pop()
            hand = hands[i % num_hands]
            hand.add(card)
        print(num_hands + ' hands have been dealt.\n')
        
    
    def is_empty(self):
        return(len(self.cards) == 0)


class Hand(Deck):


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
