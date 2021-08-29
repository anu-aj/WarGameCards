
from random import shuffle

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        print("Creating new ordered Deck")
        self.allCards=[(s,r) for s in SUITE for r in RANKS]
    def shuffle(self):
        print("Shuffling Deck")
        shuffle(self.allCards)
    def split_Half(self):
        return(self.allCards[:26],self.allCards[:26])

class hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self,cards):
        self.cards=cards
    def __str__(self):
        return "Contains {} cards".format(len(self.cards))
    def add(self,addedCards):
        self.cards.extend(addedCards)
    def remove_card(self):
        return self.cards.pop()

class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self,name,hand):
        self.name= name
        self.hand= hand
    def play_card(self):
        drawn_card=self.hand.remove_cards()
        print("{} has placed: {}".format(self.name,drawn_card))
        print("\n")
        return drawn_card
    def remove_WarCards(self):
        warCards=[]
        if len(self.hand.cards)< 3:
            return self.hand.cards
        else:
            for x in range(3):
                warCards.append(self.hand.cards.pop())
            return warCards

    def remaining_cards(self):
        """
        Return True if player still has cards left
        """
        return len(self.hand.cards)!=0

######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

#Create new deck and split it in split_Half
d=Deck()
d.shuffle()
d1,d2=d.split_Half()

#creating players
comp= Player("computer",hand(d1))

name= input("what is your name?")
user = Player(name,hand(d2))
total_rounds=0
war_count=0
while user.remaining_cards() and comp.remaining_cards():
    total_rounds+=1
    print("Time for a new round!")
    print("here are the current standings")
    print(user.name+" has the count: "+str(len(user.hand.cards)))
    print(comp.name+" has the count: "+str(len(comp.hand.cards)))
    print("Play a Card")
    print("\n")

    table_cards = []
    c_card= comp.play_card()
    p_card=user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        war_count+=1

        print("war!")

        table_cards.extend(user.remove_WarCards())
        table_cards.extend(comp.remove_WarCards())

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)
    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

print("Game Over, number of rounds:"+str(total_rounds))
print("A War Happened!")
