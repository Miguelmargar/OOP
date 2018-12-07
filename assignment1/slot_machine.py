import emoji
from random import choice
import sys

class Purse():
    """
    Purse class that holds credit amounts for user and debits and credits accordingly if win or loose
    """
    
    def __init__(self):
        self.money = 10
        
    # remove bet amount from purse
    def debit(self, amt):
        self.amt = amt
        self.money -= amt
        
    # add bet amount to purse    
    def add(self, amt):
        self.amt = amt
        self.money += amt
        
    # show balance on purse    
    def balance(self):
        return self.money