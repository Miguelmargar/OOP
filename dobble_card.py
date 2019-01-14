import emoji
from random import choice

# code given to us by lecturer to obtain emojis
imageDict = dict()
fin = open("emoji_names.txt", "r")
lines = fin.readlines()

for i, el in enumerate(lines):
    imageDict[i + 1] = emoji.emojize(el.strip())
    print(i + 1, imageDict[i + 1], end = " ")
    
    
# code given to us by lecturer to obtain an initial deck of cards with 57 cards
# nIm - 1 must be prime
# Cards must have 3, 4, 6 or 8 images
nIm = 8
n = nIm - 1
r = range(n)
rp1 = range(n+1)
c = 0
deck = {}

# first card
c += 1
card = []
for i in rp1:
    card.append(imageDict[i+1])
# card.append(i+1)
deck[c] = set(card)

# n following cards
fir j in r:
    c = c+1
#   card = [imageDict[1]]
    card = [1]
    for k in r:
        card.append(imageDict[n+2 + n*j + k])
        # card.append(n+2 + n*j + k)    
        deck[c] = set(card)
        
#  n x n following cards
for i in r:
    for j in r:
        c = c + 1
        # card = [imageDict[i+2]]
        card = [i+2]
        for k in r:
            card.append(imageDict[(n+1 + n*k + (i*k+j) % n)+1])
            # card.append((n+1 + n*k + (i*k+j)% n)+1)
            deck[c] = set(card)
print(deck)

def check_validity(deck, **kwargs):
    """
    Function to check that all cards match to each other in at least one emoji
    """
    a = set()
    b = set()
    checked = []
    # loop through the deck twice
    for card_a in deck:
        a = set(deck[card_a])
        for card_b in deck:
            b = set(deck[card_b])
            
            # don't check same decks
            if a != b:
                check_cards = b.intersection(a)
                
                # if verbose is True
                if ("verbose" in kwargs) and (kwargs["verbose"] == True):
                    print("intersection for card:", card_a, "and card", card_b, "is", check_cards)
                    
                # if no second argument given or different argument given or verbose not true
                elif not kwargs or ("verbose" not in kwargs) or (kwargs["verbose"] != True):
                    checked.append(check_cards) # appends the intersection image id
            else:
                pass
    
    print(checked)
    

class DobbleCard():
    """
    class to select one card at random from initial overall deck
    """
    # select random card from initial 'mother' deck
    def __init__(self):
        self.card = choice(list(deck.keys()))
        
    # return the card slected at random
    def give_card(self):
        return self.card
        
class DobbleDeck(DobbleCard):
    """
    class to create a deck of size selected by user na diwth main game functionality
    """
    # initiate a new deck for instance game
    def __init__(self):
        self.instance_deck = []
        
    # adds cards from DobbleCard class to new deck created
    def add_card(self):
        self.rounds = int(input("How many cards (<56)?: "))
        print("If you want to record a draw type 'd' or 'D'")
        print()
        count = self.rounds + 1
        if count <= 56:
            while count > 0:
                x = DobbleCard()
                x.give_card()
                if not deck[x.give_card()] in self.instance_deck:
                    self.instance_deck.append(deck[x.give_card()])
                    count -= 1
        else:
            print("You can't play more than 56 cards at a time, please try again")
            self.add_card()
      
    # funtion with main game functionality - display cards, get winner and keep score 
    def play_card(self):
        self.played1 = choice(self.instance_deck)
        self.remove_card(self.played1)
        self.played2 = choice(self.instance_deck)
        self.remove_card(self.played2)
        self.play_count = self.rounds + 1
        counter_a = 0
        counter_b = 0
        while self.play_count > 0:
            card1 = list(self.played1)
            card2 = list(self.played2)
            # print("this is card1", card1)
            # print("this is card2", card2)
            print()
            print(card1[0], card1[1], card1[2], "\t", card2[0], card2[1], card2[2])
            print(card1[3], card1[4], card1[5], "\t", card2[3], card2[4], card2[5])
            print(card1[6], card1[7], "\t" * 2, card2[6], card2[7])
            ask_win = input("Who wins (A or B)? ")
            if (ask_win == "a" or ask_win == "A"):
                counter_a += 1
            elif (ask_win == "b" or ask_win == "B"):
                counter_b += 1
            self.played1 = self.played2
            if not self.instance_deck == []:
                self.played2 = choice(self.instance_deck)
                self.remove_card(self.played2)
                self.play_count -= 1
                print()
            else:
                break
            
            print()
            print("score")
            print("A:", counter_a)
            print("B:", counter_b)
            
    # removes card from instance deck when played
    def remove_card(self, value):
        self.instance_deck.remove(value)
            