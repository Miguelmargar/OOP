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