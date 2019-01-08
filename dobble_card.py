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