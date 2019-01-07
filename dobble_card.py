import emoji
from random import choice

imageDict = dict()
fin = open("emoji_names.txt", "r")
lines = fin.readlines()

for i, el in enumerate(lines):
    imageDict[i + 1] = emoji.emojize(el.strip())
    print(i + 1, imageDict[i + 1], end = " ")
    
    