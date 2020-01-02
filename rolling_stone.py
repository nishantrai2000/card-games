
from classes import Deck, Card, Hand, CardGame, Suit


class RollingStoneGame():


    def __init__(self):
        deck = RollingStoneDeck()
        players = int(input('How many players?:\n'))
        if players == 4:
             deck.remove(2,3,4,5)
        hands = []
        for i in range(1, players+1):
            name = input("Player %d's name?:\n"%(i))
            hands.append(name) 
        deck.deal_hands(hands, 8)
          

class RollingStoneDeck(Deck):


    def remove(self, *values):
        for value in values:    
            for card in self.cards:
                if card.value == value:
                    self.cards.remove(card)


RollingStoneGame()        