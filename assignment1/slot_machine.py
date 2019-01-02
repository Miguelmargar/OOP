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
      
purse = Purse()  

class Column():
    """
    Column class created to randomise options results
    """
    
    def __init__(self):
        self.faces = [emoji.emojize(':red_apple:'),
                     emoji.emojize(':pear:'),
                     emoji.emojize(':tangerine:')]
        self.face = None
        
    def change_face(self):
        self.face = choice(self.faces)
        return self.face
        
class Slot(Column):
    """
    Slot class created with functionality showing 3 results, handling of purse and user input and output
    """
    
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
        
        # obtain and partially handle user input
    def take_bet(self):
        self.bet = input("how much do you bet: ")
        
        if (self.bet == "n") or (self.bet == "N"):
            self.more = False
            print("You have now exited the game")
        else:
            try:
                self.bet = int(self.bet)
            except ValueError:
                self.take_bet()
            if self.bet > purse.balance() or self.bet < 2:
                self.take_bet()
            else:
                return self.bet
                
        # handle user input within purse
    def score_slot(self):
        bet = self.bet
        if (self.a == self.b) and (self.b == self.c) and (self.a == self.c):
            purse.add(bet)
            print("your score:", (bet * 2), "- You have:", purse.balance())
            print()
        elif (self.a == self.b) or (self.a == self.c) or (self.b == self.c):
            purse.add(bet / 2)
            print("Your score:", bet * 1.5, "- You have:", purse.balance())
            print()
        else:
            purse.debit(bet)
            print("Your score: 0 - You have:", purse.balance())
            print()
            