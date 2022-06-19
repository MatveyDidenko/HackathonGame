import sys
import random

suits = ["Spades", "Clubs", "Diamonds", "Hearts"]
values = ["  2  ", "  3  ", "  4  ", "  5  ", "  6  ", "  7  ", "  8  ", "  9  ", "  10 ", "Jack ", "Queen", "King ", " Ace "]

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def getSuit(self):
        return self.suit

    def getValue(self):
        return self.value

    # def show(self):
    #     print ("{} of {}".format(self.value , self.suit))

    def show(self):
        if(self.suit == "Spades"):
            print("--------------")
            print("|             |")
            print("|   Spades    |")
            print("|     ♠       |")
            print("|     ♠       |")
            print("|   "+ self.value +"     |")
            print("|     ♠       |")
            print("|     ♠       |")
            print("|   Spades    |")
            print("|             |")
            print("--------------")
        elif(self.suit == "Clubs"):
            print("--------------")
            print("|             |")
            print("|   Clubs     |")
            print("|     ♣       |")
            print("|     ♣       |")
            print("|   "+ self.value +"     |")
            print("|     ♣       |")
            print("|     ♣       |")
            print("|   Clubs     |")
            print("|             |")
            print("--------------")
        if(self.suit == "Diamonds"):
            print("--------------")
            print("|             |")
            print("|  Diamonds   |")
            print("|     ♢       |")
            print("|     ♢       |")
            print("|   "+ self.value +"     |")
            print("|     ♢       |")
            print("|     ♢       |")
            print("|  Diamonds   |")
            print("|             |")
            print("--------------")
        elif(self.suit == "Hearts"):
            print("--------------")
            print("|             |")
            print("|   Hearts    |")
            print("|     ♡       |")
            print("|     ♡       |")
            print("|   "+ self.value +"     |")
            print("|     ♡       |")
            print("|     ♡       |")
            print("|   Hearts    |")
            print("|             |")
            print("--------------")


class Deck:
    def __init__(self):
        self.cards = []
        self.pond = []
        self.build()
        self.shuffle()

    def getPond(self):
        return self.pond

    def build(self):
        for s in suits:
            for v in values:
                self.cards.append(Card(s, v))

    def showDeck(self):
        for c in self.pond:
            c.show()

    def shuffle(self):
        temp = self.cards.copy()
        i = 0
        while len(temp) > 0:
            self.pond.append(temp.pop(random.choice(range(len(temp)))))
            i += 1

    def deal(self,player):
        for i in range(3):
            player.addCard(self.pond.pop())

    def fish(self):
        if len(self.pond) != 0:
            return self.pond.pop()
        return None

class Player:

    def __init__(self):
        self.hand = []

    def getHand(self):
        return self.hand

    def showHand(self):
        for c in self.hand:
            c.show()

    def addCard(self,card):
        self.hand.append(card)

    def ask(self,card,player):
        pass

    def reply(self,card):
        if card in self.hand:
            self.hand.remove(card)
            return True
        return False




deck = Deck()
player1 = Player()
player2 = Player()
player3 = Player()

deck.deal(player1)
deck.deal(player2)
deck.deal(player3)

player1.showHand()
player2.showHand()
player3.showHand()

def checkWin():
    player1Suits = [0, 0, 0, 0]
    player2Suits = [0, 0, 0, 0]
    player3Suits = [0, 0, 0, 0]

    for c in player1.getHand():
        if c.getSuit() == suits[0]:
            player1Suits[0] += 1
        elif c.getSuit() == suits[1]:
            player1Suits[1] += 1
        elif c.getSuit() == suits[2]:
            player1Suits[2] += 1
        elif c.getSuit() == suits[3]:
            player1Suits[3] += 1

    for a in player2.getHand():
        if a.getSuit() == suits[0]:
            player2Suits[0] += 1
        elif a.getSuit() == suits[1]:
            player2Suits[1] += 1
        elif a.getSuit() == suits[2]:
            player2Suits[2] += 1
        elif a.getSuit() == suits[3]:
            player2Suits[3] += 1

    for b in player3.getHand():
        if b.getSuit() == suits[0]:
            player3Suits[0] += 1
        elif b.getSuit() == suits[1]:
            player3Suits[1] += 1
        elif b.getSuit() == suits[2]:
            player3Suits[2] += 1
        elif b.getSuit() == suits[3]:
            player3Suits[3] += 1

    player1Pairs = 0
    player2Pairs = 0
    player3Pairs = 0
    for s in player1Suits:
        if s % 2 == 0:
            player1Pairs = s//2
            continue

    for s in player2Suits:
        if s % 2 == 0:
            player2Pairs = s//2
            continue

    for s in player3Suits:
        if s % 2 == 0:
            player3Pairs = s//2
            continue

    if((player1Pairs == 3 or player2Pairs == 3 or player3Pairs == 3) and len(deck.pond) >= 0):
        return False
    elif(len(deck.pond) >= 0):
        return True




while(True):
    checkWin()
    player1.addCard(deck.fish())
    player1.getHand()
    checkWin()
    player2.addCard(deck.fish())
    player1.getHand()
    checkWin()
    player3.addCard(deck.fish())
    player1.getHand()
