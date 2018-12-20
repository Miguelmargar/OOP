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
        

class Column():
    
    def __init__(self):
        self.faces = [emoji.emojize(':red_apple:'),
                     emoji.emojize(':pear:'),
                     emoji.emojize(':tangerine:')]
        self.face = None
        
    def change_face(self):
        self.face = choice(self.faces)
        return self.face
        
class Slot(Column):
    
    def __init__(self):
        self.more = 1
        
        self.faces = [emoji.emojize(':red_apple:'),
                     emoji.emojize(':pear:'),
                     emoji.emojize(':tangerine:')]
    
    # Create three columns  
    def pull_handle(self):
        self.a = Column.change_face(self)
        self.b = Column.change_face(self)
        self.c = Column.change_face(self)
        
    # Show faces 
    def show_slot(self):
        print(self.a + self.b + self.c)
        
        