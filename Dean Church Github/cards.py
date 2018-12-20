import random

deck = []
player1_hand = []
player2_hand = []

def makedeck(deck):
    """ populate the deck of cards"""
    SUITS = ["hearts","diamonds","clubs","spades"]
    VALUES = ["A","2","3","4","5",'6','7','8','9',"10","J",'Q',"K"]
    for e in SUITS:
        for i in VALUES:
            card = i+" "+e
            deck.append(card)


def shuffledeck(deck):
    for i in range(len(deck)):
        j=random.randrage(len(deck))
        temp = deck[i]
        deck[i] = deck[j]
        deck[j] = temp



makedeck(deck)
print(deck)
shuffledeck(deck)
print(" ")
print(deck)
