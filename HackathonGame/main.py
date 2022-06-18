import sys
import random

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

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

    def build(self):
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for v in ["  1  ", "  2  ", "  3  ", "  4  ", "  5  ", "  6  ", "  7  ", "  8  ", "  9  ", "  10 ", "Jack ", "Queen", "King ", " Ace "]:
                self.cards.append(Card(s, v))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        temp = self.cards.copy()
        i = 0
        while len(temp) > 0:
            self.pond[i] = temp.pop(random.randrange(0,len(temp),1))
            i += 1
    
    def deal(self,player):
        for i in range(5):
            player.addCard(self.pond.pop())

    def fish(self):
        if len(self.pond) != 0:
            return self.pond.pop()
        return None

class Player:
    
    def __init__(self):
        self.hand = []

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

